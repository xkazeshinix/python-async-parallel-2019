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
        self.lock = threading.Lock()    #kłódka

    def add_funds(self, value: int):
        self.funds += value
        time.sleep(0.5)

    def draw_funds(self, value: int):
        print(f'klient:{t()} wypłaca środki -- start; stan początkowy: {self.funds}')
        with self.lock:
            print(f'klient:{t()} -- przejął kłódkę')
            funs_OK = self.check_funds(value)
            if not funs_OK:
                print(f'klient:{t()} nie może wypłacić funduszy')
                return False
            time.sleep(0.5)
            self.funds -= value
            print(f'klient:{t()} -- zwalnia kłódkę')
        print(f'klient:{t()} wypłaca środki -- done; stan końcowy: {self.funds}')
        return True

    def check_funds(self, value):
        """ Sprawdza czy można wypłacić `value` bez schodzenia ze stanem konta poniżej 0"""
        print(f'klient:{t()}: sprawdzam stan konta')
        time.sleep(0.5)
        print(f'klient:{t()} odczytano stan konta: {self.funds}')
        if self.funds - value >= 0:
            return True
        else:
            return False


class MyJob(threading.Thread):
    def __init__(self, bank: Bank):
        threading.Thread.__init__(self)
        self.bank = bank

    def run(self):
        self.bank.draw_funds(10)


# bank = Bank()
# j1 = MyJob(bank)
# j2 = MyJob(bank)
#
# j1.start()
# # time.sleep(0.1)
# j2.start()
#
# j1.join()
# j2.join()

