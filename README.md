### The project for [course](https://www.udemy.com/distributed-tasks-demystified-with-celery-python/learn/v4/t/lecture/7264396?start=312). 
We will build distributed applications on python, including async tasks, multithreading, messaging, queues, Celery library, Amazon Web Services SQS, Scaling.

### Requirements
* Python 3.5
* virtualenv
* [Redis](https://redis.io/)
* Docker

#### Run virtualenv
```source ./venv/bin/activate```

#### Run Redis as Docker container
* Download [Redis image](https://hub.docker.com/_/redis/)
* Also, on redis docker page you can see how to configure the containter for your needs
* To start Redis container with persistent storage:
```
docker run -p 6379:6379 -v ~/Documents/redis-data/:/data --name aw-redis -d redis redis-server --appendonly yes
```
    
This command will run docker container with Redis and share a directory between docker container and host machine.

#### Parts
1. Pure python
2. Celery
3. Amazon Web Services SQS

#### Bugs
1. When running celery on redis 3.*, you can face a problem [AttributeError: 'float' object has no attribute 'items'](https://github.com/celery/celery/issues/5175), just install `redis==2.10.6`
 