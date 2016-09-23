from celery import Celery

BROKER_URL = 'redis://192.168.1.3:6379/0'

app = Celery('tasks', broker=BROKER_URL, backend=BROKER_URL)


@app.task
def add(x, y):
    return x + y


@app.task
def execute(code):
    gl = dict()
    exec(code, gl)
    return gl['result'] if 'result' in gl else None
