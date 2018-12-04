from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
import time
import redis

# Run with: celery -A intro_task worker --loglevel=info
# To run periodic tasks: celery -A intro_task beat --loglevel=info
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


@app.task(name='tasks.add')
def add(x, y):
    total = x + y
    print('{} + {} = {}'.format(x, y, total))
    return total


def backoff(attempts):
    """
    :param attempts:
    :return: return 1, 2, 4, 8, 16, 32
    """
    return 2 ** attempts


@app.task(bind=True, max_retries=4, soft_time_limit=5)
def data_extractor(self):
    try:
        for i in range(1, 11):
            print("Crawling HTML DOM")
            if i == 5:
                raise Exception("Crawling Index Error")
    except Exception as e:
        print("There was an exception, try again after 5 sec")
        raise self.retry(exc=e, countdown=backoff(self.request.retries))


key = "ABCCCC1231238123712636AAC"


@app.task(bind=True, name="tasks.send.email")
def send_mail_from_queue(self):
    REDIS_CLIENT = redis.Redis()
    timeout = 60 * 5  # Lock expires in 5 min
    have_lock = False
    my_lock = REDIS_CLIENT.lock(key, timeout=timeout)
    try:
        have_lock = my_lock.acquire(blocking=False)
        if have_lock:
            messages_sent = "example@mail.ex"
            print("Worker: {} \t Email message successfully send, [{}]".format(self.request.hostname, messages_sent))
            time.sleep(10)
    finally:
        print("Release resources")
        if have_lock:
            my_lock.release()


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task':     'tasks.send.email',
        'schedule': timedelta(seconds=5)
    },
}
app.conf.timezone = 'UTC'
