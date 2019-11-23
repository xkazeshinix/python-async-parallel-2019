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

# ćwiczenie: uruchomić trzykrotnie MyThread, ale tak, by całość zakończyła operację w czasie < 4s
#    (zakończyła, tzn. ostatnia linia "koniec" została wypisana do konsoli )

launched_threads = []

for i in range(10):
    t = MyThread(f'job{i}')
    t.start()
    launched_threads.append(t)

print(f'odpalone wątki: {launched_threads}')

for th in launched_threads:
    th.join()

end = time.time()
duration = end-start
print(f'całkowity czas wykonania: {duration:.6f}s')