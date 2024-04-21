class Solution {
    // 핵심: 부분 수열의 합이 절데 0보다 작을 수 없다.
    // 이유는 수열 중에 원소를 하나만 가져온다면 음수는 -1을 곱하면 양수가 되기 때문이다.

    public long solution(int[] sequence) {
        long answer = 0;

        boolean isPlus = true;

        long pulse1 = 0;
        long pulse2 = 0;

        for (int i=0; i<sequence.length; i++) {
            pulse1 += isPlus ? sequence[i] : -sequence[i];
            pulse2 += isPlus ? sequence[i] : -sequence[i];

            pulse1 = Math.max(pulse1, 0);
            pulse2 = Math.max(pulse2, 0);

            answer =  Math.max(answer, Math.max(pulse1, pulse2));

            isPlus = !isPlus;
        }

        return answer;
    }
}
