-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,
COUNT(DISTINCT O.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT O.USER_ID) / (SELECT DISTINCT COUNT(USER_ID)
                          FROM USER_INFO
                          WHERE YEAR(JOINED) = 2021), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE AS O
JOIN USER_INFO AS U
ON U.USER_ID = O.USER_ID
WHERE YEAR(JOINED) = 2021
GROUP BY YEAR, MONTH
ORDER BY YEAR ASC, MONTH ASC