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