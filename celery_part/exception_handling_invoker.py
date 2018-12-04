import sys
import os
import random

from celery.result import AsyncResult
import time

_basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(_basedir)
from intro_task import data_extractor


# Run after intro_task.py, to run: python celery_part/exception_handling.py
result = data_extractor.delay()
seconds = 0
while True:
    _result2 = AsyncResult(result.task_id)
    status = _result2.status
    print(status)
    if 'SUCCESS' in status:
        print('result after {sec} sec wait {_result2}'.format(sec=seconds,_result2=_result2.get()))
        break
    time.sleep(1)
    seconds += 1
