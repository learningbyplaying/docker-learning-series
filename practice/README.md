
# Practicing

Each option of:

https://docs.docker.com/engine/reference/commandline/run/


```
sudo docker run --name my_debian -it debian
```

```
sudo docker run --cidfile /tmp/docker_test.cid ubuntu echo "test"
```

```
sudo docker run -t -i --rm ubuntu bash
sudo docker run -it --privileged ubuntu bash
```

```
sudo docker run -w /opt -it ubuntu pwd
```

```
sudo docker run -it --storage-opt size=5G fedora /bin/bash
```

```
sudo docker run -v "$(pwd)/app:/app" -w /app -it ubuntu ls
```

```
sudo docker run -e MYVAR1=2 --env MYVAR2=foo ubuntu env
```
