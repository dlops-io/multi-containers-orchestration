
from celery import Celery
from celery.signals import worker_process_init, worker_process_shutdown, worker_ready, worker_shutdown
#import dataaccess.session as database_session
import os
import asyncio
import functools

from taskqueue.session import worker


@worker_process_init.connect
def worker_setup(*args, **kwargs):
    ...
    # loop = asyncio.get_event_loop()
    # return loop.run_until_complete(database_session.connect())


@worker_process_shutdown.connect
def worker_teardown(*args, **kwargs):
    ...
    # loop = asyncio.get_event_loop()
    # return loop.run_until_complete(database_session.disconnect())


@worker_ready.connect
def worker_start(sender, **k):
    print("Worker started...")


@worker_shutdown.connect
def worker_stop(sender, **k):
    print("Worker stopping...")