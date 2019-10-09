## Build Steps

```
git clone https://github.com/sunsong/docker-couchbase-python-env.git
cd docker-couchbase-python-env
docker build . -t docker-couchbase-python-env
docker run -ti --network ${NETWORK} -v $(pwd):/app/ docker-couchbase-python-env sh
```
