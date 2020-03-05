SELECT (months * salary) AS total_salary, COUNT(employee_id)
FROM Employee
WHERE (months * salary) = (SELECT MAX(months * salary) FROM Employee)
GROUP BY total_salary;