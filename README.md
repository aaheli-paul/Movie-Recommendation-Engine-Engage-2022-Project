# Movie-Recommendation-Engine-Engage-2022-Project
Repository for Challenge - 3 (Algorithms) project made during Microsoft Engage 2022

[![Generic badge](https://img.shields.io/badge/Engage-2022-Red.svg?style=for-the-badge)](https://acehacker.com/microsoft/engage2022/index.html) 
[![Generic badge](https://img.shields.io/badge/LinkedIn-Connect-blue.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aaheli-paul) 
[![Generic badge](https://img.shields.io/badge/Python-Language-blue.svg?style=for-the-badge)](https://github.com/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project) 
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

### Challenge - 3 : *ALGORITHMS* 

<!-- ABOUT THE PROJECT -->
#### **_Problem Description_** : 
Sorting Algorithms play an important role in recommendation engines. By the end of the project, the following questions should be answered :
- What role is played by sorting algorithms in recommendation engine.
- Which sorting algorithm is used in this project and why?

In this project, i have implemented Recommendation Engine for Movies.

<br><br><br>

<!-- APPROACH : WHAT AND WHY -->
#### **_Answering the questions_** :
> Different approaches, choosing an approach and why.

To understand the role of sorting algorithms and make a choice, one should know the different types of filtering algorithms present. They are:
1. Content-based filtering - In this, content is recommended to a user based on the past content-interaction of the same user.
2. Collaborative filtering - In this, content is recommended to a user based on the similarity of that user's content-interaction to another user's content-interaction. Users with similar activities are recommeded similar contents.
3. Hybrid filtering - This is a combination of Content-based and Collaborative filtering.

My objective was to implement an approach that would be :
- relevant to the user (content similarity)
- avoid cold start to the problem
Therefore, content-based filtering approach has been used in this project.

<!-- PROJECT PLANNING AND TRAJECTORY -->
#### _Selecting the dataset_ :
> Link to the dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/discussion?select=tmdb_5000_movies.csv

> The datasets are also available with this repo, in a folder titled *Datasets*

The following were the factors kept in mind while selecting the dataset :
- Relevant and useful data
- Different and diverse attributes (to facilitate content-based filtering approach)
- Manageable computational load

#### _Project Flow_ :
1. Dataset Analysis
2. Data Pre-processing
3. Model Building (using text vectorization and cosine similarity)
4. Model Testing
5. Establishing web connection (using streamlit)

<!-- INSTALLATIONS -->

## Getting Started
To install and run the project on your local system, following are the requirements:

### Prerequisites
Make sure to install / import the following libraries to your python environment
```sh
  install ast
  install nltk
  install pickle
```

After downloading source code files from this repo, perform the following steps:

1. Open *get_recommendation.ipynb* jupyter notebook file and change the location of datasets in the following visible lines of code :

```sh
  movies_df = pd.read_csv('C:/Users/Aaheli Paul/Movie-Recommendation-Engine-Engage-2022-Project/Datasets/tmdb_5000_movies.csv')
  credits_df = pd.read_csv('C:/Users/Aaheli Paul/Movie-Recommendation-Engine-Engage-2022-Project/Datasets/tmdb_5000_credits.csv')
```

2. Run and execute the *get_recommendation.ipynb* jupyter notebook file or run the following command on command prompt:

```sh
  python get_recommendation.ipynb
```
> After completing the execution of this file, there will be two files downloaded to the main folder : movies_list.pkl, similarity.pkl

> These files will be used during the execution of *app.py* file.

3. Run the following command on command prompt, to locally host the webpage

```sh
  streamlit run app.py
```


[![GitHub repo size](https://img.shields.io/github/repo-size/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project.svg?logo=github&style=social)](https://github.com/aaheli-paul)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project.svg?logo=git&style=social)](https://github.com/aaheli-paul/)
[![GitHub top language](https://img.shields.io/github/languages/top/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project.svg?logo=python&style=social)](https://github.com/aaheli-paul)
