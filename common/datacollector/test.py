import os
import asyncio
from time import time
from celery.utils.log import get_task_logger

from taskqueue.session import worker, async_task

logger = get_task_logger(__name__)


@worker.task(name="test_worker_task")
def test_worker_task(id):
    logger.info("Processing test_worker_task with id:"+str(id))


@async_task
async def test_worker_task_async(id):
    logger.info("Processing test_worker_task_async with id:"+str(id))
    await asyncio.sleep(5)