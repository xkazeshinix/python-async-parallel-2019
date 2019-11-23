import threading
import time


# fasdasdasd

def t():
    """Prosta funkcja podająca nazwę aktualnego wątku; skraca zapis poniżej...
        :returns nazwa wątku
    """
    return threading.current_thread().name


class MyJob(threading.Thread):
    def __init__(self, title: str):
        threading.Thread.__init__(self)
        self.title = title  # jakiś napis, który ustalamy przy uruchomieniu wątku; będzie jego własnością

    def run(self):
        print(f'title:{self.title}; nazwa:{t()} ---- start')
        time.sleep(3)
        print(f'title:{self.title}; nazwa:{t()} ---- koniec')


print(f'wątek: {t()}')  # ten kod jest wykonywany na głównym wątku (MainThread)

job1 = MyJob('sęk')
job1.start()  # uruchamiane na osobnym wątku
job1.join()  # MainThread czeka na zakończenie wątku Thread-1

job2 = MyJob('pień')
job2.start()  # uruchamiane na osobnym wątku
