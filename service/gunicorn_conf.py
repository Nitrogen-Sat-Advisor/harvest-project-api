# gunicorn configuration file

bind = '0.0.0.0:5000'
workers = 2

# Logging
loglevel = 'debug'
errorlog = 'gunicorn_error.log'
# accesslog = 'gunicorn_access.log'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
