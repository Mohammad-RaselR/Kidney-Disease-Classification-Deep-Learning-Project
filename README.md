# Kidney-Disease-Classification-Deep-Learning-Project

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Mohammad-RaselR/Kidney-Disease-Classification-Deep-Learning-Project.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidnet
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
###  dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/mrhrasel232/Kidney-Disease-Classification-Deep-Learning-Project.mlflow \
MLFLOW_TRACKING_USERNAME=mrhrasel232  \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variable: 
run this script as variable 

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/mrhrasel232/Kidney-Disease-Classification-Deep-Learning-Project.mlflow
export MLFLOW_TRACKING_USERNAME=mrhrasel232
export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0
```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

## About MLFlow & DVC

Mlflow

    - Its Porduction Grade
    - Trace all of your expleriments
    - Logging and taging your model
DVC(Data Version Control)
    - its very lite weight for POC only
    - lite weight experiments tracker
    - It can perform Orchestration (Creating Pipelines)

# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS Console

## 2. Create IAM user for deployment
    #with specific access
    1. EC2 access: It is virtual machine 
    2. ECR: Elastic Container registry to save your docker image in aws 

    #Description: About the deployment

    1. Build docker image of the source code
    2. Push your docker image to ECR
    3. Launch your EC2
    4. Pull your image from ECR in EC2
    5. Launch your docker image in EC2
    #Policy: 
    1. AmazonEC2ContainersREgistryFullAccess
    2. AmazonEC2FullAccess

## 3. Create ECR repo to stroe/save docker image
    - Save the URI: 787909119299.dkr.ecr.ap-south-1.amazonaws.com/kidney

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine: 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = kidney




