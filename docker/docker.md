---
title: "Docker Commands"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Docker is a container service. Arguably *the* container service.
- Docker Cheat Sheet [here](https://github.com/wsargent/docker-cheat-sheet#registry--repository)
- This video is useful for getting [started](https://www.youtube.com/watch?v=W3bk2pojLoU)
- Docker containers vs. VMs (https://stackoverflow.com/questions/16047306/how-is-docker-different-from-a-normal-virtual-machine?rq=1)

# Concepts
* dockerfile - a list of commands that builds a series of images, resulting in a named image that you can use to start a container
* image - the bits that need to be instanced to form a container
* dangling image - an image without a name [https://stackoverflow.com/questions/45142528/docker-what-is-a-dangling-image-and-what-is-an-unused-image]
* container - an instance of a running image
* entry point - the program that will be ruuning
* container states - containers can be "created", "up" or "exited" [https://stackoverflow.com/questions/43734412/what-does-created-container-mean-in-docker]


# Windows
- Docker uses a single hyper-v, and thus is subject to any hyper-v nuances and limitations
- When docker is running there will be tray app running where you can get some info
- However most interaction with docker is via command line, be it cmd, powershell, or some form of bash


# Basic commands
* `docker -?`                  ( list all commands)
* `docker -v`                  (version)
* `docker version`             (long client/server version)
* `docker -p2`                 (list running containers)
* `docker search tensorvlow`   (search docker hub for an imagte)
* `docker ps`                  (see what dockers are running)
* `docker kill containername`  (kill a particular container)
* `docker ps -a`               (see running and exited container)
* `docker rm containername`    (remove an exited container)
* `docker -i`                  (allocate a pseudo-tty)
* `docker -t`                  (keep STDIN open even if not attached)
* `docker -e`                  (set environment variable)
* `docker images`
* `docker rm -v $(docker ps -a -q -f status=exited)` (delete all stopped containers)
* `docker rm -f $(docker ps -qa`) (delete all stopped and running containers)

# Useful commands 
* docker exec -it tf /bin/bash  # Open a terminal on a docker

# Useful 
* `sudo usermod -aG docker user_name`  # gets rid of need for sudo for docker
* `docker run --name tf -p:8888:8888 -v //d/tensorflow/notebooks:/notebooks tensorflow/tensorflow`
* `docker run --name tf -p:8888:8888 -v //d/tensorflow/boltzmann-machines:/rbms tensorflow/tensorflow`


# Docker foreground/background process killing advice
- See the comments from GHETTO.CHILD in his answer
- https://stackoverflow.com/questions/32224101/kill-a-running-process-like-a-webserver-inside-a-docker-container-without-killin
