#!/bin/bash
pwd="$(pwd)"
docker run -it -p 8080:8080 -v "$pwd"/code:/app hldbackend /bin/bash
