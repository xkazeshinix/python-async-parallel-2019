from dataclasses import dataclass
from flask import jsonify


@dataclass
class Accounts:
    account_no: int
    secret: str
    funds: int


class Lehman:
    def __init__(self):
        self.accounts = [
            Accounts(account_no=1, secret='account1', funds=100),
            Accounts(account_no=2, secret='account_2', funds=200),
            Accounts(account_no=3, secret='account_3', funds=300),
            Accounts(account_no=4, secret='account_4', funds=400),
            Accounts(account_no=5, secret='account_5', funds=500),
            Accounts(account_no=6, secret='account_6', funds=600),
        ]

    def validate_account(self, account_no, secret):
        acc = self.get_acc(account_no)

        if acc.secret == secret:
            return acc

        raise Exception('Pass invalid')

    def get_acc(self, acc_no):
        for acc in self.accounts:
            if acc.account_no == acc_no:
                return acc
        raise Exception('User not found')

    def get_funds(self, account_no, secret):
        try:
            acc = self.validate_account(account_no, secret)

            if acc:
                return jsonify({'funds': acc.funds})
        except Exception:
            return jsonify({'info': 'permission denied'})

    def draw_funds(self, account_no, secret, amount):
        try:
            acc = self.validate_account(account_no, secret)

            if acc:
                if acc.funds > 0 and amount <= acc.funds:
                    acc.funds -= amount
                    return jsonify({'info': 'amount withdrawed', 'funds': acc.funds})
                return jsonify({'info': 'amount cannot be withdrawed', 'funds': acc.funds})
        except Exception:
            return jsonify({'info': 'permission denied'})

    def add_funds(self, account_no, secret, amount):
        try:
            acc = self.validate_account(account_no, secret)

            if acc:
                acc.funds += amount
                return jsonify({'info': 'amount added', 'funds': acc.funds})

        except Exception:
            return jsonify({'info': 'permission denied'})

    def transfer_funds(self, account_no, secret, amount, second_acc):
        try:
            acc = self.validate_account(account_no, secret)

            if acc:
                if acc.funds > 0 and amount <= acc.funds:
                    for sec_acc in self.accounts:
                        if sec_acc.account_no == second_acc:
                            acc.funds -= amount
                            sec_acc.funds += amount
                            return jsonify({'info': 'amount transfered', 'funds': acc.funds})

                return jsonify({'info': 'amount cannot be transfered', 'funds': acc.funds})
        except Exception:
            return jsonify({'info': 'permission denied'})
