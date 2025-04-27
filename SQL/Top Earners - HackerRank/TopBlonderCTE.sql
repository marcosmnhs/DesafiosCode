WITH Earnings AS (
    SELECT salary * months AS total_earnings
    FROM employee
), 
Max_earning AS (
    SELECT MAX(total_earnings) AS max_earning
    FROM Earnings
)
SELECT m.max_earning, COUNT(*) AS CONT
FROM Earnings e
JOIN Max_earning m
ON m.max_earning = e.total_earnings;