import json
import time
from typing import Dict
import threading
from flask import Flask, jsonify, request

from threads.bank import Bank

app = Flask(__name__)
bank = Bank()


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





app.run(host='localhost', port=5001, debug=None, load_dotenv=False)  # can skip all args
