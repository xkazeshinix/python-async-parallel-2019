import threading
import time

def t():
    """Prosta funkcja podająca nazwę aktualnego wątku; skraca zapis poniżej...
        :returns nazwa wątku
    """
    return threading.current_thread().name


class Bank:
    def __init__(self):
        self.funds = 15

    def add_funds(self, value: int):
        self.funds += value
        time.sleep(0.5)

    def draw_funds(self, value: int):
        print(f'klient:{t()} wypłaca środki -- start; stan początkowy: {self.funds}')
        self.funds -= value
        time.sleep(0.5)
        print(f'klient:{t()} wypłaca środki -- done; stan końcowy: {self.funds}')


class MyJob(threading.Thread):
    def __init__(self, bank: Bank):
        threading.Thread.__init__(self)
        self.bank = bank

    def run(self):
        self.bank.draw_funds(10)


bank = Bank()
j1 = MyJob(bank)
j2 = MyJob(bank)

j1.start()
j2.start()

j1.join()
j2.join()

