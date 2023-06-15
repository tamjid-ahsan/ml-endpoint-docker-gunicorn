# ml-endpoint-docker-nginx
Details coming soon

# Instruction

## build image from Dockerfile

``` bash
docker build -t ml-model-churn .
```

## run server

``` bash
docker run -d -p 5000:5000 ml-model-churn
```

## previously run container

```bash
docker start <CONTAINER> # eloquent_boyd
```

## list all running

``` bash
docker ps
```

## reference:

[docker-using-flask](https://medium.com/swlh/machine-learning-model-deployment-in-docker-using-flask-d77f6cb551d6)
