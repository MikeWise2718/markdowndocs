---
title: "Docker Commands"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Docker is a container service. Arguable *the* container service.
Docker Cheat Sheet [here](https://github.com/wsargent/docker-cheat-sheet#registry--repository)
This video is useful for getting [started](https://www.youtube.com/watch?v=W3bk2pojLoU)


# Concepts
* image - the bits that need to be instansced to form a container
* contatiner - an instance of a running image

# Basic commands
* docker -?                  ( list all commands)
* docker -v                  (version)
* docker version             (long client/server version)
* docker -p2                 (list running containers)
* docker search tensorvlow   (search docker hub for images)
* docker ps                  (see what dockers are running)
* docker kill containername  (kill a particular container)
* docker ps -a               (see running and exited container)
* docker rm containername    (remove an exited container)
* docker -i                  (allocate a pseudo-tty)
* docker -t                  (keep STDIN open even if not attached)
* docker -e                  (set environment variable)

# Open a terminal on a docker
docker exec -it tf /bin/bash

# Useful 
* docker run --name tf -p:8888:8888 -v //d/tensorflow/notebooks:/notebooks tensorflow/tensorflow
* docker run --name tf -p:8888:8888 -v //d/tensorflow/boltzmann-machines:/rbms tensorflow/tensorflow