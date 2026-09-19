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