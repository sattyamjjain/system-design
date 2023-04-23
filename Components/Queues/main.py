import queue
import time
import threading


def process_queue(q):
    while True:
        item = q.get()
        print(f"Processing item {item}...")
        time.sleep(1)
        q.task_done()


q = queue.Queue()
for i in range(5):
    t = threading.Thread(target=process_queue, args=(q,))
    t.daemon = True
    t.start()

for i in range(10):
    q.put(i)

q.join()
print("All items processed")
