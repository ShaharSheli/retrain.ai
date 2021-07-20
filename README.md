# retrain.ai

![image](https://user-images.githubusercontent.com/64142727/126201869-8b4507fc-3156-4665-9037-92f4a6e0c0d5.png)

ML Pipeline Steps:
1. Data transformation & validation - perform sanity checks and data structure transformations
2. Model training - load transformed data and train model
3. Model testing - load test data and test trained model on it

## Project Architecture:

base_docker.dockerfile - base image that includes the correct python version, requirements installed and data copied

data folder:
- Dockerfile - based on the base_docker, this docker includes python codes that check the data and transfrom it to be ready for the model
- data.py - python code to check and transform it

training folder:
- Dockerfile - based on the base_docker, this docker includes the python codes which load the joblib of the transformed data and train the model
- train.py - python code which used to load the transformed data and train the model

test folder:
- Dockerfile - based on the base_docker, this docker includes the python codes that transfrom the test data and test the model
- test.py - python code which used to load, transform and test the model

## Implementation:
In my current job we are using Tekton to create, monitor and run pipelines.
Tekton suggest a catalog of ready-to-use images of steps in order to implement simple tasks.
In this task I would use the dockerfiles to create my own steps and connect them to a full pipeline with conditional step that will be executed only if the previous step ended successfully.
Additionally, I can use parameters in Tekton to allow choosing different datasets and algorithms to reuse the pipeline at scale or run several trains or tests in parallel.
