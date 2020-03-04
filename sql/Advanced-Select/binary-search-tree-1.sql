SELECT N as newN,
    CASE 
        WHEN P IS NULL THEN 'Root'
        WHEN P IS NOT NULL AND (SELECT COUNT(N) FROM BST WHERE P = newN) > 0 THEN 'Inner'
        WHEN (SELECT COUNT(N) FROM BST WHERE P = newN) = 0 THEN 'Leaf'
    END
FROM BST
ORDER BY N;