import threading
import time
import random

_queue = [] # NOT THREAD SAFE
MAX_ITEMS = 10
condition = threading.Condition()


class ProducerThread(threading.Thread):
    def run(self):
        numbers = range(MAX_ITEMS)  # Generate num in 0..5
        global _queue  # Global queue

        while True:
            condition.acquire()
            if len(_queue) >= MAX_ITEMS:
                print("Queue is full, producer is waiting")
                condition.wait()  # If full, just wait
                print("Space in queue, Consumer notified producer")
            number = random.choice(numbers)
            _queue.append(number)
            print("Produced {}, queue: {}".format(number, _queue))
            condition.notify()  # Notify consumers
            condition.release()
            time.sleep(random.random())


class ConsumerThread(threading.Thread):
    def run(self):
        global _queue
        while True:
            condition.acquire()
            if not _queue:
                print("Nothing in queue, consumer is waiting")
                condition.wait()
                print("Producer added something to queue and notified consumer")
            number = _queue.pop(0)
            print("Consumed {}, queue: {}".format(number, _queue))
            condition.notify()  # Notify producer
            condition.release()
            time.sleep(random.random())

if __name__ == "__main__":
    producer = ProducerThread()
    producer.daemon = True
    producer.start()

    consumer = ConsumerThread()
    consumer.daemon = True
    consumer.start()

    producer.join()
    consumer.join()