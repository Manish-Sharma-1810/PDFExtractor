#!/bin/bash

# Set default values for environment variables
DEFAULT_AWS_REGION="us-east-1"
DEFAULT_IMAGE_NAME="manishdocker1810/pdfextractor:v1.0"

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Override default values if environment variables are provided
AWS_REGION=${AWS_REGION:-$DEFAULT_AWS_REGION}
BUCKET_NAME=${BUCKET_NAME}
IMAGE_NAME=${IMAGE_NAME:-$DEFAULT_IMAGE_NAME}

START_PORT=5001
END_PORT=5002

# Build docker image
docker build -t $IMAGE_NAME $SCRIPT_DIR

for ((i = $START_PORT; i <= $END_PORT; i++)); do
    docker container run -d --name pdfextractor_$i -p $i:5000 -e AWS_REGION=$AWS_REGION -e BUCKET_NAME=$BUCKET_NAME --restart on-failure $IMAGE_NAME
done

# Create volume for the portainer container
docker volume create portainer_data

# Run portainer container
docker container run -d --name portainer -p 8080:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
