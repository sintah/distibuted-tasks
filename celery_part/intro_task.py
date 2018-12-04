from celery import Celery
import time

# Run with celery -A intro_task worker --loglevel=info
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
