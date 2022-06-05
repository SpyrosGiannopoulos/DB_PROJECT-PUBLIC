USE DB_PROJECT;
/* δημιουργία όψης που εμφανίζει τα έργα που δουλεύει ένας ερευντής*/
DROP VIEW if exists proj_research;
CREATE VIEW proj_research AS
 select p.project_id, r.researcher_id, p.title, r.first_name, r.last_name
 from projects p INNER JOIN researchers r on p.researcher_id=r.researcher_id
 union
 select p.project_id, r.researcher_id, p.title, r.first_name, r.last_name
 from projects p inner join works_on w on p.project_id=w.project_id
 inner join researchers r on w.researcher_id=r.researcher_id
 order by researcher_id;
 
 select first_name, last_name, title from proj_research;
 
