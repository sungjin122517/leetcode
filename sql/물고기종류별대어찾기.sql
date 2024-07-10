SELECT FI.ID, FNI.FISH_NAME, FI.LENGTH
FROM FISH_INFO FI
JOIN FISH_NAME_INFO FNI
ON FI.FISH_TYPE = FNI.FISH_TYPE
-- GROUP BY FISH_INFO.ID, FISH_NAME_INFO.FISH_NAME
WHERE (FI.FISH_TYPE, FI.LENGTH) IN (
    SELECT FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)
ORDER BY FI.ID