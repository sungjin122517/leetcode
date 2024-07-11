-- 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로
-- FILE ID 기준 내림차순

-- 조회수가 가장 높은 중고거래 게시물 가져오기는 했지만, 첨부파일 string 만드는 건 못 했다.

-- 배운점
-- HAVING 절은 GROUP BY 절과 함께 사용되어 집계 결과를 필터링할 때 쓰인다.

SELECT
    CONCAT('/home/grep/src/', F.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE F
JOIN USED_GOODS_BOARD B
ON F.BOARD_ID = B.BOARD_ID
WHERE VIEWS = (
    SELECT MAX(VIEWS)
    FROM USED_GOODS_BOARD
)
ORDER BY F.FILE_ID DESC