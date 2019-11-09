from flask import Flask, jsonify, request

app = Flask(__name__)


# https://www.tutorialspoint.com/flask/flask_http_methods.htm


@app.route('/status')
def get_json_data():
    return jsonify({'comment': 'App działa OK'})


@app.route('/compute')
def compute():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'sum': a + b, 'difference': a - b})


app.run(host='localhost', port=5001, debug=None, load_dotenv=False)  # can skip all args
