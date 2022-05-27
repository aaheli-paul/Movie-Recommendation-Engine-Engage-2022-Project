# Movie-Recommendation-Engine-Engage-2022-Project
Repository for Challenge - 3 (Algorithms) project made during Microsoft Engage 2022

[![Generic badge](https://img.shields.io/badge/Engage-2022-Red.svg?style=for-the-badge)](https://acehacker.com/microsoft/engage2022/index.html) 
[![Generic badge](https://img.shields.io/badge/LinkedIn-Connect-blue.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aaheli-paul) 
[![Generic badge](https://img.shields.io/badge/Python-Language-blue.svg?style=for-the-badge)](https://github.com/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project) 
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

### Challenge - 3 : *ALGORITHMS* 

#### **_Problem Description_** : 
Sorting Algorithms play an important role in recommendation engines. By the end of the project, the following questions should be answered :
- What role is played by sorting algorithms in recommendation engine.
- Which sorting algorithm is used in this project and why?

In this project, i have implemented Recommendation Engine for Movies.

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

#### _Selecting the dataset_ :
> Link to the dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/discussion?select=tmdb_5000_movies.csv
> The datasets are also available with this repo, in a folder titled *Datasets*

The following were the factors kept in mind while selecting the dataset :
- Relevant and useful data
- Different and diverse attributes (to facilitate content-based filtering approach)
- Manageable computational load

#### Project Flow :
1. Dataset Analysis
2. Data Pre-processing
3. Model Building (using text vectorization and cosine similarity)
4. Model Testing
5. Establishing web connection (using streamlit)

> Credits: https://www.netflixprize.com/rules.html

#### The goal of this project is to develop a recomendation system [#DataScience](https://github.com/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project) for Netflix.

[![GitHub repo size](https://img.shields.io/github/repo-size/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project.svg?logo=github&style=social)](https://github.com/aaheli-paul)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project.svg?logo=git&style=social)](https://github.com/aaheli-paul/)
[![GitHub top language](https://img.shields.io/github/languages/top/aaheli-paul/Movie-Recommendation-Engine-Engage-2022-Project.svg?logo=python&style=social)](https://github.com/aaheli-paul)
