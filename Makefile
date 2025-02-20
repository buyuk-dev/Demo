# Variables for environment
DOCKER_IMAGE_NAME=haiku-generator

AZURE_OPENAI_API_KEY=
AZURE_OPENAI_BASE_URL=
AZURE_OPENAI_DEPLOYMENT_NAME=
AZURE_OPENAI_API_VERSION=

# Recipe to build the Docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME) .

# Recipe to run the Docker container
run: build
	docker run \
	    -e AZURE_OPENAI_BASE_URL=$(AZURE_OPENAI_BASE_URL) \
	    -e AZURE_OPENAI_API_KEY=$(AZURE_OPENAI_API_KEY) \
	    -e AZURE_OPENAI_DEPLOYMENT_NAME=$(AZURE_OPENAI_DEPLOYMENT_NAME) \
	    -e AZURE_OPENAI_API_VERSION=$(AZURE_OPENAI_API_VERSION) \
	    $(DOCKER_IMAGE_NAME)