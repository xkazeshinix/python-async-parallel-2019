from flask import Flask, jsonify, request

from bank import Bank
from config import magic, server_port, server_host

app = Flask(__name__)
bank = Bank()


@app.route('/')
@app.route('/status')
def get_json_data():
    return jsonify({'comment': f'Bank działa OK'})


@app.route('/funds/get')
def get_funds():
    return jsonify({'funds': bank.funds})


@app.route('/funds/draw')
def draw_funds():
    amount = int(request.args.get('amount'))
    operation_OK = bank.draw_funds(amount)
    return jsonify({'OK': operation_OK, 'comment:': ''})

print(f'magic:{magic}')
app.run(host=server_host, port=server_port, debug=None, load_dotenv=False)  # can skip all args
