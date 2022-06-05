USE DB_PROJECT;

#Οι ερευνητές που εργάζονται σε 5 ή περισσότερα έργα που δεν έχουν παραδοτέα(όπου αυτο μεταφράζεται σε ένα παραδοτέο)

SELECT cust.researcher_id, cust.first_name, cust.last_name, count(cust.project_id) as counter from(
SELECT R.researcher_id, P.project_id, R.first_name, R.last_name, 
count(*) AS deliverable_counter
FROM RESEARCHERS R INNER JOIN WORKS_ON W ON
R.researcher_id = W.researcher_id INNER JOIN PROJECTS P ON W.project_id = P.project_id 
INNER JOIN DELIVERABLES D ON D.project_id=P.project_id 
GROUP BY R.researcher_id, P.project_id
HAVING deliverable_counter = 1 
UNION SELECT R.researcher_id, P.project_id, R.first_name, R.last_name, 
count(*) as deliverable_counter
FROM RESEARCHERS R INNER JOIN PROJECTS P 
ON P.researcher_id=R.researcher_id INNER JOIN DELIVERABLES D 
ON D.project_id=P.project_id 
GROUP BY R.researcher_id, P.project_id
HAVING deliverable_counter=1 ) cust
GROUP BY cust.researcher_id HAVING counter>=5 order by counter DESC, researcher_id;