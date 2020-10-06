# Bootcamp Graduation Project
### Date Completed: 10/2/2020

# Description
Per the projects description: "For the next two weeks, you'll be a junior analyst who's about to solve their first real tasks from major customers. You'll work simultaneously on a big project and on minor tasks, much like in real life."

## File Structure


    |-- README.md
    |-- ABtestAnalyses-SubProject
    |   |-- ABTestAnalysis.ipynb 
    |   |-- README.md
    |   |-- images
    |       |-- ------>REMOVED TO SHORTEN Contains images of charts to show on README<---------
    |-- SQL-SubProject
        |-- README.md
        |-- SQL-SubProject.ipynb
        |-- images
            |-- ------>REMOVED TO SHORTEN Contains images of charts and dashboard to present on markdown<---------
    |-- RFMCustomerSegmentation-MainProject
    |   |-- graduationProjectCode.ipynb
    |   |-- graduationProject_Presentation.pptx
    |-- images
    |   |-- ------->REMOVED TO SHORTEN Contains images of charts and dashboard to to show on README<---------
    
    
## ----------------------------------Main Project -----------------------------------------
## <a href="https://public.tableau.com/profile/daniel.garcia.rodriguez#!/vizhome/graduationProject/RFMDashboard">Link</a> to dashboard solution.

# 1. Introduction

## 1.1 Business Goal
Identify and form segments of customers based on similar purchasing characteristics (from transcational data) to inform the sales and marketing strategy of the company. Hypothetically speaking, the company is interested in profiles for customers located in the U.K. where the majority of their customers are located in. In terms of currency, the company hypothetically requested that it be in U.S. dollar rather than in pounds. Lastly, the company also requested that the analysis to be based on one year (here defined as year from the last day of transaction recorded in the dataset).

## 1.2 Method Overview

Segment users based on their consumer profiles using RFM and produced dashboard for hypothetical client (online store marketing and sales team). My mains steps:
1. Got a general idea of the underlying data through basic exploration steps
2. Dealt with missing values, erroneous or faulty data (ie. negative values), dropped duplicates, and changed data types.
3. Carried out exploratory data analysis. Explored the distribution of variables (ie. `quantity`) over time (date, month) and per unique customer.
4. Preprocessed and conducted an exploratory clustering analysis of the products; used Facebook's fastText unsupervised alogorithm to create vectors from product name and then applied K-means on the result (no statistical tests were done to test K-means clustering performance.
5. Used RFM model to segment customers. 
6. Exported relevant data from analysis and created a Tableau dashboard as a deliverable for hypothetical stakeholder.

### Figures

#### Figure 2.
<img src="images/Screenshot_429.png?raw=true" width="40%" height="50%"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Screenshot_430.png?raw=true" width="40%" height="50%"/>

#### Figure 3.
<img src="images/Screenshot_431.png?raw=true" width="55%" height="40%"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Screenshot_432.png?raw=true" width="25%" height="25%"/>

#### Figure 5.
<img src="images/Screenshot_433.png?raw=true" width="60%" height="40%"/>

#### Figure 6.
<img src="images/Screenshot_434.png?raw=true" width="60%" height="40%"/>

#### Figure 7.
<img src="images/Screenshot_436.png?raw=true" width="40%" height="50%"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Screenshot_437.png?raw=true" width="40%" height="50%"/>

#### Figure 8.
<img src="images/Screenshot_438.png?raw=true" width="40%" height="50%"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Screenshot_440.png?raw=true" width="40%" height="50%"/>

#### Figure 9.
<img src="images/Screenshot_439.png?raw=true" width="30%" height="45%"/>

