SELECT FLAVOR
FROM (SELECT * FROM FIRST_HALF 
UNION ALL 
SELECT * FROM JULY) AS FLAVOR_ALL
GROUP BY FLAVOR_ALL.FLAVOR
ORDER BY SUM(FLAVOR_ALL.TOTAL_ORDER) DESC
LIMIT 3