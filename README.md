# Python Flask Chatbot Web-App using OpenAI API

## Requirements
> pip install --no-cache-dir -r requirements.txt


## /css & /js --- Bootstrap Frontend Framework for UI
[Bootstrap v5.3](https://getbootstrap.com/docs/5.3/getting-started/download/) --- downloaded .css (CSS) and .js (JavaScript) files under /css & /js


## /static & /templates
/static --- customized static resources (customized CSS & JavaScript files)\
/templates --- HTML template files, used together with Backend framework


## main.py
Python Script for Flask (A lightweight backend framework) Web-App


## Dockerfile
For building image of this project (during building: use --build-arg OPENAI_API_KEY=xxxxxx to set the API key, or the building will fail)


## chatbot-deployment.yaml & chatbot-service.yaml
Deployment and service configurations for the k8s cluster, to run a k8s cluster of this project

to set docker hub secret for k8s:
>kubectl create secret docker-registry my-dockerhub-secret-name \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=myusername \
  --docker-password=mypassword \
  --docker-email=myemail@example.com