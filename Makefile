NAME   := jchukwum/ai-fitted-removebg
TAG    := $(shell git log -1 --pretty=format:"%h")
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:${TAG}

build:
	@docker build -t ${IMG} .
	@docker tag ${IMG} ${LATEST}

push:
	@docker push ${LATEST}

login:
	@docker log -u ${DOCKER_USER} -p ${DOCKER_PASS}
