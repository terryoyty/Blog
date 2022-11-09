
bind = '0.0.0.0:8000'

worker_class = 'Blog.wsgi'  # 还可以使用gevent模式，还可以使用sync模式，默认sync模式

# workers = multiprocessing.cpu_count() * 2 + 1 # 并行工作进程数
workers = 2  # 并行工作进程数
threads = 1  # 指定每个工作者的线程数

backlog = 2048  # 监听队列

timeout = 120  # 超过多少秒后工作将被杀掉，并重新启动。一般设置为30秒或更多

worker_connections = 1000  # 设置最大并发量

daemon = False  # 默认False，设置守护进程，将进程交给supervisor管理

debug = True

loglevel = 'debug'
accesslog = '/var/log/gunicorn/access.log'
# access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" " "%(a)s"'  # 设置gunicron访问日志格式，错误日志无法设置
errorlog = '/var/log/gunicorn/error.log'
# logger_class = 'gunicron.gologging.Logger'

preload_app = True  # 预加载资源

autorestart = True


# gunicorn -c gunicorn.py main:app -k uvicorn.workers.UvicornWorker
