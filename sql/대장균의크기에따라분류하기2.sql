-- 비율을 한 번에 구할 수 있나, 아니면 order by 해서 구분 해야하나?
-- NTILE은 파티션을 설정할 수 있어 파티션 갯수에 따라 순위를 나누어준다.

SELECT
    A.ID,
    CASE
        WHEN A.COLONY_LEVEL = 1 THEN 'CRITICAL'
        WHEN A.COLONY_LEVEL = 2 THEN 'HIGH'
        WHEN A.COLONY_LEVEL = 3 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS 'COLONY_NAME'
FROM (
    SELECT
        ID,
        NTILE(4)
    OVER (
        ORDER BY SIZE_OF_COLONY DESC
    ) AS 'COLONY_LEVEL'
    FROM ECOLI_DATA
) AS A
ORDER BY
    A.ID