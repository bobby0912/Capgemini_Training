import threading


chunks = []
n = int(input("Enter n to calculate sum of n values: "))
limit = 0
n += 1
while (n >= 1000):
    chunks.append(list(range(limit, limit+1000)))
    print(f"limit added {limit}, {limit+1000}")
    limit += 1000
    n -= 1000
if (n != 0):
    chunks.append(list(range(limit, limit+n)))
    print(f"limit added {limit}, {limit+n}")


results=[]

def calculateSum(chunk):
    print("Started calculating.")
    result=sum(chunk)
    print("completed.")
    results.append(result)


threads=[]
for chunk in chunks:
    thread=threading.Thread(target=calculateSum,args=(chunk,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(sum(results))

print("Task completed.")

