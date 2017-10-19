Hybrid Music Recommender System using Apache Spark and Python

Description

A recommender system that will recommend new songss to a user based on their listening history. Suggesting different songs or musical artists to a user is important to many music streaming services, such as Pandora and Spotify. In addition, this type of recommender system could also be used as a means of suggesting TV shows or movies to a user (e.g., Netflix).


##### Project timeline: 
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
Step 2: investigate into the data, transform unstructured data to structured
Step 3: preprocess, feature engineering 
Step 4: 

#### Collaborative filtering
utility matrix for song frequency
Counts of users: 264713 
Counts of songs: 1559988 

Key learnings：
1. use pyspark for big data processing; efficient for large data 
2. troubleshoot noisy dataset and extract useful information 
3. design the recommender system to maximize efficiency and effectiveness; also for scalability consideration




