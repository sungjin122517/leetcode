# 11055. 가장 큰 증가하는 부분 수열

n = int(input())
seq = list(map(int, input().split()))
sums = [0 for _ in range(n)]
sums[0] = seq[0]

# loop을 어떻게 돌려야할지 헷갈린다
for i in range(n):
    for j in range(i):
        # print('seq[i]:', seq[i], 'seq[j]:', seq[j])
        if seq[i] > seq[j]:
            sums[i] = max(sums[i], sums[j] + seq[i])
            # print('if sums[i]:', sums[i])
        else:
            sums[i] = max(sums[i], seq[i])
            # print('else sums[i]:', sums[i])

print(max(sums))
