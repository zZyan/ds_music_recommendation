## Hybrid Music Recommender System using Apache Spark and Python
### Author: Yan Zhu

#### Description

A recommender system that will recommend new songss to a user based on their listening history. Suggesting different songs or musical artists to a user is important to many music streaming services, such as Pandora and Spotify. In addition, this type of recommender system could also be used as a means of suggesting TV shows or movies to a user (e.g., Netflix).


#### Project timeline: 
Sep.24 2017: design the system (modified as the project goes)
Sep.25 2017: design the data pipeline
Sep.31 2017: finished data cleaning
Oct.13 2017: finished collaborative filtering 


####  Designning 
Key consideration for designing the system 
1. speed and time efficiency
2. (related to 1) scalability - use distributed dataframe
3. old start scenario 


#### Data pipeline
Step 1: get data, unzip files
- use AWS Athena to extract all zipped files and save into seperate tables for Play, Down, Search

Step 2: investigate into the data, transform unstructured data to structured
- load csv to python, clean the data slightly and save to seperate csv 
- challenge: large files for play, cannot be load into python, or sql server
- solution: python script to write into table line by line 

Step 3: preprocess, feature engineering

Step 4: build model

#### Collaborative filtering
utility matrix for song frequency
Counts of users: 264713 
Counts of songs: 1559988 

Key learnings：
1. use pyspark for big data processing; efficient for large data 
2. troubleshoot noisy dataset and extract useful information 
3. design the recommender system to maximize efficiency and effectiveness; also for scalability consideration

##### Unsuccessful experiments log:
1. preprocessing: download csv to local (expensive to do sql manupilation on AWS and also needs cleaning, potentially can be done in SQL)
2. preprocessing: setup microsoft sql management platform: very slow and confusing syntax 
3. model: utility matrix with a) plain play frequency; b) log(frequency); c) log(frequency)+ int(bool download) 



