SQL Problem 6 – Histogram of Tweets

Source: Ace the Data Science Interview – SQL Chapter

Problem Description

Given a table named tweets, write an SQL query to generate a histogram of tweets posted by users in the year 2022.

The objective is to group users based on the total number of tweets they posted in 2022 and calculate how many users belong to each group.

Table Schema

Table Name: tweets

Column	Data Type
tweet_id	INTEGER
user_id	INTEGER
msg	STRING
tweet_date	TIMESTAMP
Expected Output
tweet_bucket	users_num
1	2
2	1
Explanation
User 111 posted 2 tweets in 2022.
User 254 posted 1 tweet in 2022.
User 148 posted 1 tweet in 2022.

Therefore, 2 users fall into the 1-tweet bucket, while 1 user falls into the 2-tweet bucket.

SQL Concepts Practiced
Filtering records using WHERE.
Extracting year from timestamps.
Aggregate functions using COUNT().
Grouping records using GROUP BY.
Nested queries and multi-level aggregation.
Learning Objective

Practice multi-level aggregation in SQL by calculating individual user activity and generating a frequency distribution based on tweet counts.
