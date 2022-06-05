USE DB_PROJECT;


#έργα που χρηματοδοτούνται σε ένα επιστημονικό πεδίο τον τελευταίο χρόνο (έχουμε μόνο ενεργά έργα)

SET @selected_field = 2;

SELECT P.project_id, P.title FROM PROJECTS P INNER JOIN DESCRIBES D 
ON (P.project_id=D.project_id AND D.field_id=@selected_field)
WHERE (P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE())
ORDER BY p.project_id;

#ερευνητές που δουλεύουν σ'αυτό τον τελευταίο χρόνο (έχουμε μόνο ενεργά έργα)

SELECT P.project_id, R.researcher_id, R.first_name, R.last_name FROM PROJECTS P INNER JOIN DESCRIBES D 
ON (P.project_id=D.project_id AND D.field_id=@selected_field) INNER JOIN RESEARCHERS R 
ON P.researcher_id = R.researcher_id WHERE (P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE())
UNION
SELECT P.project_id, R.researcher_id, R.first_name, R.last_name FROM PROJECTS P INNER JOIN DESCRIBES D 
ON (P.project_id=D.project_id AND D.field_id=@selected_field)
INNER JOIN WORKS_ON W ON P.project_id=W.project_id INNER JOIN RESEARCHERS R 
ON W.researcher_id=R.researcher_id WHERE (P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE())
Order by project_id;