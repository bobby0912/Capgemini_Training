import threading,time
def deamonTask():
    while True:
        print("Deamon started running.")
        time.sleep(1)

deamon_thread=threading.Thread(target=deamonTask,daemon=True)
deamon_thread.start()

time.sleep(5)
print("main thread exit.")