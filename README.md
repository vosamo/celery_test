## 用来测试Celery的简单例子

采用Celery做异步任务调度，用rabbitmq作broker和保存任务结果。

## 依赖

- Python 2.7.10
- Celery 3.1.23
- RabbitMQ-server 3.3.5-17.el7

依赖安装:`pip install celery`，`yum -y install rabbitmq-server`

## 使用说明：

将本仓库克隆到本地，解压缩；打开两个shell终端，进入celery_test目录。

启动worker：在一个终端中输入`celery worker -A tasks --loglevel=info`

在另一个终端中执行python tasks.py，可以看到任务日志。
