# dfs로 풀면 비효율적. 하나하나씩 들어가보면서 최댓값을 찾기위해 계속 비교해야 하니깐.
# 하지만 경로를 묻지 않고 최댓값만 묻는 문제였으니 dp

def solution(triangle):
    # height = len(triangle)
    
    # # convert 2d triangle list to 1d
    # newT = sum(triangle, [])
    # arr = [0]*len(newT)

    # arr[0] = triangle[0]
    # for i in range(height):
    #     arr[2*i+1] = newT[i] + newT[2*i+1]
    #     arr[2*i+2] = newT[i] + newT[2*i+2]

    # # return max element from the last 'height' number of elements from arr
    # return max(arr[-height:])

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])