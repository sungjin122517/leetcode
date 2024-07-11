-- group by food_type

-- 배운점
-- GROUP BY는 MAX 함수까지 커버하지 못 한다. (sum, count는 가능)
-- GROUP BY 후 MAX를 하면 최댓값이 아닌 테이블 최상단 값을 가져온다.
-- use subquery!

-- https://monawa.tistory.com/125
-- https://monawa.tistory.com/126

-- SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES) AS FAVORITES
-- FROM REST_INFO
-- GROUP BY FOOD_TYPE
-- ORDER BY FOOD_TYPE DESC

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (
    SELECT FOOD_TYPE, MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC