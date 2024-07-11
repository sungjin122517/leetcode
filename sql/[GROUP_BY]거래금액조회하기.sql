-- 조건에 맞는 사용자와 총 거래금액 조회하기

-- 거래 총 금액 > 700000
-- 회원 ID, 닉네임, 총거래금액
-- ORDER BY 총거래금액

-- status가 done인 애들만 골라서 sum 하고, 70만원 넘는 애들로만 선별

SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_USER AS U
ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE'
GROUP BY U.USER_ID -- 중복 user id가 있으니깐 묶어야한다
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES