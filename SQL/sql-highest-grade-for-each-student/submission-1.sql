-- Write your query below
-- WITH cte AS 
-- (
--     SELECT student_id,exam_id,score,
--      RANK() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id) AS rnk
--     FROM exam_results
-- )
-- SELECT student_id,exam_id,score
-- FROM cte
-- WHERE rnk = 1;
SELECT student_id, MIN(exam_id) as exam_id, MAX(score) as score
FROM exam_results
WHERE (student_id, score)
IN
(SELECT student_id, MAX(score) as max_score
FROM exam_results
GROUP BY student_id)
GROUP BY student_id