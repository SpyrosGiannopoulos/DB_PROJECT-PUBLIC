USE DB_PROJECT;


/*εύρεση όλων των προγραμμάτων */
select program_id, program_name from programs order by program_id; 


/*εύρεση ενεργών έργων την ημερομηνιά που έχει επιλέξει ο χρήστης*/
SET @user_date = '2022-06-03';
SELECT project_id,title FROM PROJECTS WHERE (start_date < @user_date AND due_date > @user_date)
ORDER BY project_id; 


/*SELECT R.researcher_id, R.first_name, R.last_name FROM RESEARCHERS R INNER JOIN PROJECTS P ON (start_date < @user_date AND due_date > @user_date)
INNER JOIN WORKS_ON W ON (P.project_id=W.project_id AND W.researcher_id=R.researcher_id);*/


/*εύρεση όλων των ερευνητών που δουλεύον στο έργο που έχει επιλέξει ο χρήστης*/
SET @selected_project = 3;
SELECT P.researcher_id, R.first_name,R.last_name FROM PROJECTS P INNER JOIN RESEARCHERS R 
WHERE (@selected_project=P.project_id AND R.researcher_id=P.researcher_id)
UNION
SELECT R.researcher_id, R.first_name, R.last_name FROM RESEARCHERS R INNER JOIN WORKS_ON W 
ON (@selected_project=W.project_id AND W.researcher_id=R.researcher_id) ;


/*εύρεση όλων των έργων με διάρκεια που έχει επιλέξει ο χρήστης*/
SET @project_duration= DATE_SUB(CURRENT_DATE(),INTERVAL -2 YEAR) - CURRENT_DATE() ;
SELECT project_id, title FROM PROJECTS WHERE (due_date-start_date)<@project_duration
order by project_id;


/*εύρεση έργων που διαχειρίζεται ένας στέλεχος*/
SET @exec_proj = 2;
SELECT project_id, title FROM PROJECTS WHERE executive_id=@exec_proj
order by project_id;