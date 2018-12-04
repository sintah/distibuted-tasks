import threading
import time
import random
import queue

MAX_ITEMS = 10
_queue = queue.Queue(MAX_ITEMS)


class ProducerThread(threading.Thread):
    def run(self):
        numbers = range(MAX_ITEMS)  # Generate num in 0..5
        global _queue  # Global queue

        while True:
            number = random.choice(numbers)
            _queue.put(number)
            print("Produced {}, queue size: {}".format(number, _queue.qsize()))
            time.sleep(random.random())


class ConsumerThread(threading.Thread):
    def run(self):
        global _queue
        while True:
            number = _queue.get()
            _queue.task_done()
            print("Consumed {}, queue size: {}".format(number, _queue.qsize()))
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
