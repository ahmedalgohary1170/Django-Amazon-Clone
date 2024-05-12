from celery import shared_task
import time


@shared_task
def execute_somthing():
    for i in range(10):
        print(i)
        time.sleep(1)