import threading

# Race condition - when multiple processes or threads read and write data imtes concurrently
# Solutions:
# 1. mutual exclusion(one process at a time gets in critical section)
# 2. message passing (message sent through shared data structure consisting of queues. Exclusive locks by a dedicated consumer per message

# Celery?
#

# Mutex

counter_buffer = 0
counter_lock = threading.Lock()

COUNTER_MAX = 100

def consumer1_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        counter_lock.acquire()
        #Critical section
        counter_buffer += 1
        counter_lock.release()

def consumer2_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        counter_lock.acquire()
        #Critical section
        counter_buffer += 1
        counter_lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=consumer1_counter)
    t2 = threading.Thread(target=consumer2_counter)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final counter buffer is {}".format(counter_buffer))