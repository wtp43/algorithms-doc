# Celery
- Separate api and db tasks
- db tasks do not support parallel transactions, needs 1 session per worker: celery prefork is used which is multiprocessing
	- but cores are limited
- we don't want to block tasks because of a db connection
- api tasks that don't require a db connection are used with multithreading instead
-  