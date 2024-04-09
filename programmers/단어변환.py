def solution(begin, target, words):
    visited = [False for i in range(len(words))]

    def bfs(words, begin, target):
        queue = []
        queue.append([begin, 0]) # 시작 단어와 단계 0
        # visited[start] = 0
        while queue:
            curr, step = queue.pop(0)
            
            if curr == target:
                return step
            
            for word in words:
                count = 0
                for i in range(len(word)):
                    if curr[i] != word[i]:
                        count += 1
                
                if count == 1:
                    queue.append([word, step+1])
    
    if target not in words:
        return 0
    return bfs(words, begin, target)
            

    answer = 0
    return answer