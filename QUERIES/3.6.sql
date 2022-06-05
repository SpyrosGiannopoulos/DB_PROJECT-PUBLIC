USE DB_PROJECT;
# όλοι οι ερευνητές κάτω των 40 που δουλεύουν στα περισσότερα έργα
select cust.r_id, cust.r_fn, cust.r_ln, cust.r_pr, sum(cust.project_count) as s_pr from
(SELECT R.researcher_id as r_id, R.first_name as r_fn, R.last_name as r_ln, W.project_id as r_pr, count(*) as project_count FROM RESEARCHERS R
INNER JOIN WORKS_ON W ON (R.researcher_id = W.researcher_id AND 
DATE_SUB(R.date_of_birth,INTERVAL -40 YEAR)> CURRENT_DATE())
INNER JOIN PROJECTS P ON P.project_id=W.project_id and P.start_date<CURRENT_DATE() AND
P.due_date>CURRENT_DATE() 
GROUP BY R.researcher_id 
UNION
SELECT R.researcher_id as r_id, R.first_name as r_fn, R.last_name as r_ln, P.project_id as r_pr, count(*) project_count FROM RESEARCHERS R
INNER JOIN PROJECTS P ON R.researcher_id = P.researcher_id AND 
DATE_SUB(R.date_of_birth,INTERVAL -40 YEAR)> CURRENT_DATE()
AND P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE() 
GROUP BY R.researcher_id ) as cust
group by (cust.r_id) order BY s_pr DESC ;