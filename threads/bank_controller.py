from flask import Flask, jsonify, request

from bank import Bank
from zaliczenie import Lehman
from config import magic, server_port, server_host
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bank = Bank()
lehman = Lehman()


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


@app.route('/funds/add')
def add_funds():
    amount = int(request.args.get('amount'))
    operation_OK = bank.add_funds(amount)
    return jsonify({'OK': operation_OK, 'comment:': ''})


@app.route('/accounts/<acc_no>/get')
def get_lehman_funds(acc_no):
    secret = request.args.get('secret')
    return lehman.get_funds(int(acc_no), secret)


@app.route('/accounts/<acc_no>/draw')
def draw_lehman_funds(acc_no):
    secret = request.args.get('secret')
    amount = int(request.args.get('amount'))

    return lehman.draw_funds(int(acc_no), secret, amount)


@app.route('/accounts/<acc_no>/add')
def add_lehman_funds(acc_no):
    secret = request.args.get('secret')
    amount = int(request.args.get('amount'))

    return lehman.add_funds(int(acc_no), secret, amount)


@app.route('/accounts/<acc_no>/transfer')
def transfer_lehman_funds(acc_no):
    secret = request.args.get('secret')
    amount = int(request.args.get('amount'))
    sec_acc = int(request.args.get('sec_acc'))

    return lehman.transfer_funds(int(acc_no), secret, amount, int(sec_acc))


print(f'magic:{magic}')
app.run(host=server_host, port=server_port, debug=None, load_dotenv=False)  # can skip all args
