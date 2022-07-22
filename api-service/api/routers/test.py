from os import name
from fastapi import APIRouter, Depends, Path, Query

from datacollector import test

router = APIRouter()


@router.get(
    "/test_route1"
)
async def test_route1():
    print("test_route1 ...")

    # Call a celery task
    task = test.test_worker_task.delay(id=1234)

    print(task)

    return {
        "task": task.id
    }

@router.get(
    "/test_route2"
)
async def test_route2():
    print("test_route2 ...")

    # Call a celery task
    task = test.test_worker_task_async.delay(id=4567)
    print(task)

    return {
        "task": task.id
    }