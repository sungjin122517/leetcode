-- parent_id가 자신의 id와 일치하는 행의 개수를 새 child_count 열과 함께 출력하기.
-- null은 ifnull 구문 등을 사용하여 0으로 대체하여 출력.

-- 

SELECT ID, IFNULL(
    (SELECT COUNT(*)
     FROM ECOLI_DATA
     GROUP BY PARENT_ID
     HAVING PARENT_ID = ID
    ), 0
) AS CHILD_COUNT
FROM ECOLI_DATA
ORDER BY ID