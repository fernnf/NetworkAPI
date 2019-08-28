DOCKER_PRJ=networkapi:latest
DOCKER_NAME=networkapi
DOCKER_APP=docker

build:
	$(DOCKER_APP) build --no-cache -t $(DOCKER_PRJ) .
 
run:
	$(DOCKER_APP) run -d  --name $(DOCKER_NAME) --privileged -p 8000:8000 $(DOCKER_PRJ)

del:
	$(DOCKER_APP) stop $(DOCKER_NAME) && $(DOCKER_APP) rm $(DOCKER_NAME) 
