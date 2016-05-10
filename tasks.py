#!/usr/bin/env python
# coding=utf-8
from celery import Celery
from time import sleep

#app = Celery('tasks', backend='amqp', broker='amqp://')
app = Celery('tasks')
app.config_from_object('celeryconfig')
@app.task
def add(x,y):
    sleep(5)
    return x + y

if __name__ == '__main__':
    res = add.delay(3,4)
    print "task id:", res.id
    print res.get()
