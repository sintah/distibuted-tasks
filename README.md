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
docker run -v ~/Documents/redis-data/:/data --name aw-redis -d redis redis-server --appendonly yes
```
    
This command will run docker container with Redis and share a directory between docker container and host machine.

### Tasks
1. Blocking 
2. Non-blocking
3. Consumer producer problem