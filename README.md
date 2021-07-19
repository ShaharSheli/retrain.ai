# retrain.ai

![image](https://user-images.githubusercontent.com/64142727/126201869-8b4507fc-3156-4665-9037-92f4a6e0c0d5.png)

ML Pipeline steps:
1. Data transformation & validation - preform sanety checks and transform data structure to be preperd for the model
2. Model training - load the transformed data and fit the model
3. Model testing - load test data and test the fitted model on it

Project architecture:

base_docker.dockerfile - base image that included the correct python version, requirements installed and data copied

data folder:
- data_docker.dockerfile - based on the base_docker, this docker includes the python codes that check the data and transfrom it to be ready for the model
- data.py - python code to check and transfrom it

training folder:
- model_training.dockerfile - based on the base_docker, this docker includes the python codes that load the dill of the transfromed data and train the model
- train.py - python code to load the transformed data and fit the model

test folder:
- test_model.dockerfile - based on the base_docker, this docker includes the python codes that transfrom the test data and 
- test.py - python code to load,transfrom and test the model
