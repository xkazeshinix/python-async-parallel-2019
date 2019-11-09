import threading
import time
import random

def shop_for(article: str):
    print(f'thread: {threading.current_thread().name} shopping for {article}')
    time.sleep(1.2)
    print(f'bought {article}')


def execute(i):
    print(f'Execution of Thread {i} {threading.current_thread().name} started')
    sleep_time = random.randint(1, 4)
    time.sleep(sleep_time)
    print(f'Execution of Thread {i} finished')


for i in range(4):
    thread = threading.Thread(target=execute, args=(i,))
    thread.start()
    print('Active Threads:', [t.ident for t in threading.enumerate()])

threading.Thread(target=shop_for, args=('bread',)).start()
