import threading
import time


class MyThread(threading.Thread):
    def __init__(self, title: str):
        threading.Thread.__init__(self)
        self.title = title

    def run(self):
        print(f'wątek o tytule {self.title}; nazwa:{threading.current_thread().name}')
        time.sleep(1.3)
        print(f'wątek o tytule {self.title}; nazwa:{threading.current_thread().name} ---- koniec')


print(f'główny wątek: {threading.current_thread().name}')

t1 = MyThread('pierwszy')
t2 = MyThread('drugi')

t1.start()
t1.join()
