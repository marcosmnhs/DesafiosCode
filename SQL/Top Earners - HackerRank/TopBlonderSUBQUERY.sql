SELECT (salary * months) AS max_earning, COUNT(*)
FROM employee
WHERE (salary * months) = (SELECT MAX(salary * months) FROM employee);