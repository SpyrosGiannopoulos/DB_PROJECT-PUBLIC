USE DB_PROJECT;

#Tα 3 κορυφαία ζεύγη επιστημονικών πεδίων που εμφανίστηκαν σε έργα

select S.field_name, F.field_name, cust.counter from (
SELECT A.field_id as newField_A, B.field_id as newField_B ,B.project_id, count(*) as counter FROM DESCRIBES A INNER JOIN DESCRIBES B 
ON (A.project_id = B.project_id AND  A.field_id<B.field_id AND A.description_id <> B.description_id)
GROUP BY A.field_id, B.field_id ORDER BY counter DESC limit 3) cust
inner join scientific_fields S
on S.field_id= cust.newField_A
inner join scientific_fields F on F.field_id=cust.newField_B
order by cust.counter DESC;