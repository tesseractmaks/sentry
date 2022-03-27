import threading
import time

from multiprocessing.pool import ThreadPool

sem = threading.Semaphore()


def fun1():
    while True:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2():
    while True:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)


if __name__ == '__main__':
    try:
        with ThreadPool(processes=3) as pool:
            thread_1 = pool.apply_async(fun1)
            thread_2 = pool.apply_async(fun2)
            thread_1.get()
            thread_2.get()
    except KeyboardInterrupt:
        pass
    





        


