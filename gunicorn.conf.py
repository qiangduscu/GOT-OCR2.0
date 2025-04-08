# gunicorn.conf.py
bind = "0.0.0.0:8080"
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 300
reload = True