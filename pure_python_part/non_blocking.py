import time
import threading

# Run methods in two different threads without joining to main thread

def count_down(count):
    print("Start counting down from {} to 0".format(count))
    while count >= 0:
        print("Counting down buddy!\tCurrent:\t{}\tThread: {}".format(count, threading.current_thread().name))
        count -= 1
        time.sleep(1)


def count_up(count):
    print("Start counting up from 0 to {}".format(count))
    cnt = 0
    while cnt <= count:
        print("Counting up buddy!\t\tCurrent:\t{}\tThread: {}".format(cnt, threading.current_thread().name))
        cnt += 1
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(name="countDown", args=(10, ), target=count_down)
    t2 = threading.Thread(name="countUp", args=(15,), target=count_up)
    t1.start()
    t2.start()
    print("All done")
