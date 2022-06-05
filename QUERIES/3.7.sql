USE DB_PROJECT;

#Τop 5 στελέχη που έχουν δώσει τη μεγαλύτερη χρηματοδότηση σε μια εταιρεία (company)

SELECT E.executive_id, E.executive_first_name, E.executive_last_name, O.org_name, SUM(P.funding) Total_funds
FROM EXECUTIVES E INNER JOIN PROJECTS P ON E.executive_id = P.executive_id INNER JOIN ORGANIZATIONS O
ON P.organization_id = O.organization_id INNER JOIN COMPANIES C ON C.organization_id=O.organization_id
GROUP BY E.executive_id ORDER BY Total_funds DESC
limit 5;