import json
from typing import Dict

from flask import Flask, jsonify, request

app = Flask(__name__)

# https://www.tutorialspoint.com/flask/flask_http_methods.htm

# ładowanie konfiguracji aplikacji (opcjonalne, ale to dobry pomysł);
# po zbudowaniu aplikacji (poniżej) file "config.json" powinien się znajdować w folderze aplikacji
with open('config.json', 'r') as f:
    loaded = json.load(f)
    magic = loaded['magic']


@app.route('/status')
def get_json_data():
    return jsonify({'comment': f'App działa OK; magic:{magic}'})


# dostępna pod: http://localhost:5001/compute?a=10&b=0
@app.route('/compute')
def compute():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if b == 0:
        # teraz zwracamy komunikat o błędzie, oraz http error-code 400 (BAD_REQUEST)
        return jsonify({'comment': 'b==0, cannot divide'}), 400
    return jsonify({'sum': a + b, 'difference': a - b, 'division': a / b})


# dostępna pod: http://localhost:5001/welcome/roadrunner/suffix/nice%20to%20meet%20you
@app.route('/welcome/<username>/suffix/<message>')
def welcome(username, message):
    return jsonify({'comment': f'Hello {username}, {message}!'})


class Auth:
    def __init__(self, user: str, pass_: str):
        self.user = user
        self.pass_ = pass_


# zadanie -> zbierać userów w jakieś strukturze (np. liście 'users', albo Dict lub Set),
#   i zwrócić błąd jeśli tworzymy usera, którego pole "user" już zostało "zajęte"
# rozwiązanie:

users: Dict[str, Auth] = {}


# dostępna per Postman (trzeba zrobić zapytanie POST):
# localhost:5001/user/create
# w sekcji "body" trzba dać "raw -> JSON", i w polu JSON dodać:
# {
# 	"user": "Xi Wuhan",
# 	"pass_": "123"
# }
@app.route('/user/create', methods=['POST'])
def create_user():
    data = request.json
    k = Auth(**data)
    if users.keys().__contains__(k.user):
        return jsonify({'comment': 'This user name already exists!'}), 400
    users[k.user] = k
    return jsonify(k.__dict__)


app.run(host='localhost', port=5001, debug=None, load_dotenv=False)  # can skip all args

# możliwa kompilacja do pojedynczego pliku wykonywalnego:
# `pyinstaller _zero.py -n my_flask_app --onefile
