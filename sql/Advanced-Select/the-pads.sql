SELECT CONCAT(name, '(', SUBSTRING(occupation, 1, 1), ')' ) as name
FROM OCCUPATIONS
ORDER BY name ASC;
SELECT CONCAT('There are a total of', ' ', COUNT(occupation), ' ', LOWER(occupation), 's.' ) as total
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY total;
