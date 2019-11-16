import threading
import time


class MyThread(threading.Thread):
    def __init__(self, title: str):
        threading.Thread.__init__(self)
        self.title = title

    def run(self):

        print(f'wątek o tytule {self.title}; nazwa:{threading.current_thread().name}')
        time.sleep(3)
        print(f'wątek o tytule {self.title}; nazwa:{threading.current_thread().name} ---- koniec')


print(f'główny wątek: {threading.current_thread().name}')

# start
start = time.time()

t1 = MyThread('pierwszy')
t2 = MyThread('drugi')

# ćwiczenie: uruchomić trzykrotnie MyThread, ale tak, by całość zakończyła operację w czasie < 4s
#    (zakończyła, tzn. ostatnia linia "koniec" została wypisana do konsoli )
t1.start()
t2.start()
t1.join()

end = time.time()
duration = end-start
print(f'całkowity czas wykonania: {duration:.6f}s')