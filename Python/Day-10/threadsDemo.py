import threading 
import time

def task1():
    i=0
    while(i<=10):
        print(i)
        i+=2
        time.sleep(1)

def task2():
    j=1
    while(j<=10):
        print(j)
        j+=2
        time.sleep(1)

thread1=threading.Thread(target=task1)
thread2=threading.Thread(target=task2)
thread1.start()
thread1.join()
thread2.start()
thread2.join()

print("main thread completed.")