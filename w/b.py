import threading
import time
from typing import Dict

d = threading.local()

class Magazyn:
    def __init__(self):
        self.storage = {}

    def store(self, article):
        print(f'wątek {threading.current_thread().name} magazynuje artykuły; local:{d.x}')
        if not self.storage.__contains__(article):
            self.storage[article] = 0
        self.storage[article] += 1


magazyn = Magazyn()


class WorkerThread(threading.Thread):
    def __init__(self, mag: Magazyn, article: str):
        threading.Thread.__init__(self)
        self.magazyn = mag
        self.article = article

    def run(self):
        print(f' Kupuję: {self.article}, wątek: {threading.current_thread().name}')
        if self.article == 'bitcoin':
            subthread = WorkerThread(magazyn, 'wallet')
            subthread.start()
            subthread.join()
        time.sleep(0.3)
        d.x = threading.current_thread().name
        print(d.x)
        self.magazyn.store(self.article)

        print(f' OK;  wątek: {threading.current_thread().name}')


thread1 = WorkerThread(magazyn, 'chleb')
thread2 = WorkerThread(magazyn, 'mleko')
thread3 = WorkerThread(magazyn, 'bitcoin')
thread1.start()
thread1.join()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("Exiting Main Thread")
print(f'magazyn: {magazyn.storage}')
