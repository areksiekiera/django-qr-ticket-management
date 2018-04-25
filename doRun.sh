#!/bin/bash

docker run -it -p 80:80 --net=host --rm --env-file=.env -v $(pwd)/app:/home/docker/code/app float
