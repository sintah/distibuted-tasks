import time


# Run blocking method in 1 thread
def count_down(count):
    print("Start counting down from {} to 0".format(count))
    while count >= 0:
        print("Counting down buddy! {}".format(count))
        count -= 1
        time.sleep(1)


if __name__ == "__main__":
    count_down(10)
    count_down(5)
    print("All done")
