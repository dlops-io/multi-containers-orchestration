import os
import asyncio
import functools
from celery import Celery


REDIS_URL = os.environ["REDIS_URL"]

# Setup the celery worker
#worker = Celery('worker', broker=REDIS_URL)
worker = Celery('worker', broker=REDIS_URL, include=[
    "datacollector.test"
])

def async_task(task, name="", timeout=None):
    @worker.task(name=name)
    @functools.wraps(task)
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()

        future = asyncio.wait_for(
            task(*args, **kwargs),
            timeout=timeout,
            loop=loop
        )

        return loop.run_until_complete(future)

    return wrapper