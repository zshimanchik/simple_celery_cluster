from tasks import execute
from random import randint
import time


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


args = [randint(10**3,10**5) for _ in range(10)]
main(args)