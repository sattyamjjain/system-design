from celery import Celery
import time

app = Celery('tasks', broker='pyamqp://guest@localhost//')

app.conf.update(
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
)


@app.task
def long_task(duration):
    time.sleep(duration)
    return f'Task completed after {duration} seconds'


if __name__ == '__main__':
    result1 = long_task.delay(5)
    result2 = long_task.delay(10)
    result3 = long_task.delay(15)
    print(f'Task 1 status: {result1.status()}')
    print(f'Task 2 status: {result2.status()}')
    print(f'Task 3 status: {result3.status()}')
    print(result1.get())
    print(result2.get())
    print(result3.get())
