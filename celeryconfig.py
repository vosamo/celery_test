#!/usr/bin/env python
# coding=utf-8
BROKER_URL = 'amqp://'    # broker设置
CELERY_RESULT_BACKEND = 'amqp://'    # 存储元数据和返回值的后端
CELERY_TASK_SERIALIZER = 'json'    # 内容格式为json
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
CELERY_IMPORTS = ("tasks",)    # 列出worker需要import的模块
