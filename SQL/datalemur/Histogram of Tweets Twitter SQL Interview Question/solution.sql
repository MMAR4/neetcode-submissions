SELECT tweet_count_per_user,COUNT(user_id) AS users_num
FROM
  (
    SELECT user_id, 
    COUNT(tweet_id) AS tweet_count_per_user 
    FROM tweets 
    WHERE YEAR(tweet_date) = 2022
    GROUP BY user_id
  ) AS t
GROUP BY tweet_count_per_user
;
