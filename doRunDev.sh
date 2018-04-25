#!/bin/bash

docker run -it -p 8000:8000 --net=host --rm --env-file=.env -v $(pwd)/app:/home/docker/code/app float bash
