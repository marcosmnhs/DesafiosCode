SELECT p.firstName, p.lastName, a.city, a.state
FROM person AS p
LEFT JOIN address a 
ON p.personid = a.personid;
