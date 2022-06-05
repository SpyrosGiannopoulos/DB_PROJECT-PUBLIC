USE DB_PROJECT;

#Oργανισμοί που έχουν λάβει τον ίδιο αριθμό έργων σε διάστημα δύο συνεχόμενων ετών, με τουλάχιστον i έργα ετησίως


select l.con1 as organization_name, l.cy2 as first_year, l.cy1 as second_year, l.c1 as no_of_projects from
(SELECT  cust.o_name as con1, cust.y2 as cy2, cust.y1 as cy1, count(distinct cust.p1_id) AS c1 
from (select p1.project_id as p1_id ,p2.project_id as p2_id, p1.organization_id as o1_id, o.org_name as o_name,  YEAR(p2.start_date) as y2,YEAR(p1.start_date) as y1
 from projects p1 inner join projects p2 on p1.organization_id=p2.organization_id
and p1.project_id<>p2.project_id and (YEAR(p1.start_date)-YEAR(p2.start_date))=1 inner join organizations o on o.organization_id=p1.organization_id) cust 
GROUP BY cust.o1_id, cust.y2,cust.y1) as l 
inner join
(SELECT  cust.o_name as con2, cust.y2 as cy21, cust.y1 as cy11, count(distinct cust.p2_id) AS c2 
from (select p1.project_id as p1_id ,p2.project_id as p2_id, p1.organization_id as o1_id, o.org_name as o_name,  YEAR(p2.start_date) as y2,YEAR(p1.start_date) as y1
 from projects p1 inner join projects p2 on p1.organization_id=p2.organization_id
and p1.project_id<>p2.project_id and (YEAR(p1.start_date)-YEAR(p2.start_date))=1 inner join organizations o on o.organization_id=p1.organization_id) cust
 GROUP BY cust.o1_id, cust.y2, cust.y1) as m 
 on l.c1=m.c2 and l.con1=m.con2 and l.cy2=m.cy21 and l.cy1=m.cy11 and l.c1>1 order by l.c1 DESC 
