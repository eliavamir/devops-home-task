# DevOps Home Task - CI/CD Pipeline

This project implements a complete, automated CI/CD pipeline using Terraform, Jenkins, Docker, and AWS EC2 to deploy a containerized Python Flask web application.

---

## 🏗️ Project Architecture & Structure

- `/app`: Python Flask web application, unit tests (`pytest`), linter checks (`flake8`), and a multi-stage `Dockerfile`.
- `/infra`: Terraform configuration files (`main.tf`, `variables.tf`, `outputs.tf`, `providers.tf`) to provision AWS infrastructure (VPC, Security Groups, Jenkins EC2, and App EC2).
- `/jenkins`: Jenkins declarative pipeline script (`Jenkinsfile`) managing the CI/CD lifecycle.

---

## 🚀 Prerequisites
- AWS Account with configured CLI credentials (`aws configure`)
- Terraform CLI installed locally
- Docker Hub account
- An AWS EC2 Key Pair named `devops-key` (or update `infra/variables.tf`)

---

## 🛠️ Step-by-Step Setup Instructions

### 1. Provision Infrastructure via Terraform
Navigate to the infrastructure directory, initialize Terraform, and apply the configuration:
```bash
cd infra
terraform init
terraform apply

2. Jenkins Setup & Configuration
Access your Jenkins server via browser: http://<JENKINS_PUBLIC_IP>:8080.

Install recommended plugins during initial setup and create an admin user.

Configure the required credentials in Jenkins (Manage Jenkins -> Credentials):

Add your Docker Hub credentials.

Add your SSH private key (devops-key.pem) for connecting to the app server.



3. Running the CI/CD Pipeline
Create a new Pipeline job in Jenkins.

Link it to your GitHub repository and point it to the Jenkinsfile in the root directory.

Click Build Now to trigger the pipeline.

The pipeline automatically executes the following stages:

Code Checkout: Pulls the latest code from GitHub.

Lint Check: Runs flake8 to verify code style.

Run Unit Tests: Executes pytest to ensure code stability.

Build & Push Docker Image: Builds the multi-stage Docker image and pushes it to Docker Hub.

Deploy to App Server: Connects via SSH, pulls the latest image, stops the old container, and spins up the new container.

Health Check: Performs a curl request to verify the application is up and running.




🔌 API Endpoints
GET /: Returns "Hello, DevOps!"

POST /echo: Returns the input JSON payload.