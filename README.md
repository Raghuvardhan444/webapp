# CI/CD Pipeline with Local Infrastructure Automation

This project demonstrates how to set up a CI/CD pipeline for a simple Flask web application using GitHub Actions, Docker, and Ansible.

## Features

- Basic Flask web application.
- Dockerized infrastructure for local deployment.
- CI/CD pipeline using GitHub Actions.
- Configuration management with Ansible.

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>



## Build and run the Docker container:

docker build -t flask-app .
docker run -p 5000:5000 flask-app



##  CI/CD Pipeline

The pipeline is triggered on every push to the main branch.
Steps in the pipeline:

 Build: Ensures the app builds successfully.

 Test: (Placeholder for unit tests).

 Deploy: Uses Docker and Ansible to deploy the app.


## Files Overview

app.py: Flask web application code.
requirements.txt: Python dependencies.
Dockerfile: Builds the Docker image.
ansible-playbook.yml: Configures and deploys the application using Ansible.
.github/workflows/main.yml: GitHub Actions workflow for CI/CD.


## Challenges
Setting up Ansible modules for Docker requires installing the community.docker.
Ensuring GitHub Actions runners had Docker installed.
