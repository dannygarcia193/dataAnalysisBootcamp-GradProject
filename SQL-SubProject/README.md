# SQL-SubProject
Queried external database using SQL and analyzed results using python.

Data completed: August, 2020


**Project description:** 
Hello this is my submission for the AB Test sub-project (part of the graduation project) submission from Practicum by Yandex's Data Analyst program. You can find more about the Data Analyst by clicking [here.](https://practicum.yandex.com/data-analyst/)
 
>The coronavirus took the entire world by surprise, changing everyone's daily routine. City dwellers no longer spent their free time outside, going to cafes and malls; more people were at home, reading books. That attracted the attention of startups that rushed to develop new apps for book lovers.

>You've been given a database of one of the services competing in this market. It contains data on books, publishers, authors, and customer ratings and reviews of books. This information will be used to generate a value proposition for a new product.

## Goal
This information will be used to generate a value proposition for a new product.

## Task and Answers

- Find the number of books released after January 1, 2000.
  - A large portion of the books in the database were released in the 2000s.
- Find the number of user reviews and the average rating for each book.
  - On average, books are reviewed by 2 users and are left with a rating of 4/5. Books on the aggregate seem to have a favorable rating considering the low % 1-2 ratings.
- Identify the publisher that has released the greatest number of books with more than 50 pages (this will help you exclude brochures and similar publications from your analysis).
  - Penguin books has the most number of book releases (42) for books with > 50 pages.
- Identify the author with the highest average book rating (look only at books with at least 50 ratings).
  - The top 3 authors with the highest average book rating having at least 50 user ratings are: J.K. Rowling/Mary GrandPré, Markus Zusak/Cao Xuân Việt Khương, and J.R.R. Tolkien.
- Find the average number of text reviews among users who rated more than 50 books.
  - There are on average roughly 24 number of text reviews among users who rated more than 50 books.
  
### Figures

#### Figure 1.
<img src="images/Screenshot_442.png?raw=true" width="80%" height="80%"/>

#### Figure 2.
<img src="images/Screenshot_443.png?raw=true" width="70%" height="70%"/>

#### Figure 3.
<img src="images/Screenshot_444.png?raw=true" width="80%" height="80%"/>
