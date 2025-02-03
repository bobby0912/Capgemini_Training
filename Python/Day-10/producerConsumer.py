import threading,queue,time

def producer(q):
    for i  in range(10):
        q.put(i)
        print(f"{i} is produced.")
        time.sleep(2)


def consumer(q):
    while True:
        item=q.get()
        if(item is None):
            break
        # data=q.get()
        print(f"{item} is consumed.")
        time.sleep(2)

q=queue.Queue()
producer=threading.Thread(target=producer,args=(q,))
consumer=threading.Thread(target=consumer,args=(q,))

producer.start()
consumer.start()

producer.join()
q.put(None)
consumer.join()

print("Task completed.")