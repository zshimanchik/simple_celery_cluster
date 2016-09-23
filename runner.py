from tasks import execute
from random import randint
import time
from celery.signals import task_success


def main(args):
    code = open('code.py', 'r').read()
    tasks = []
    for arg in args:
        task = execute.delay(code.format(arg=arg))
        task.args = arg
        tasks.append(task)

    while any(not task.ready() for task in tasks):
        for task in tasks[:]:
            if task.ready():
                print("{} -> {}".format(task.args, task.get()))
                tasks.remove(task)
        time.sleep(1)

    for task in tasks:
        print("{} -> {}".format(task.args, task.get()))
    print("done")


args = [randint(10**2,10**3) for _ in range(3)]
main(args)