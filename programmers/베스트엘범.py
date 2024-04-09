# from collections import deque


def solution(genres, plays):
    answer = []
    # key and value를 뭐로 정해야하나
    # key=genre, value=sum of plays로 하면 장르의 순서는 구할 수 있는데
    # 고유 번호를 모른다
    genre_tot = {}
    genre_dic = {}
    
    for i in range(len(genres)):
        if genres[i] in genre_tot.keys():
            genre_tot[genres[i]] += plays[i]
            genre_dic[genres[i]].append((plays[i], i))
        else:
            genre_tot[genres[i]] = plays[i]
            genre_dic[genres[i]] = [(plays[i], i)]
    
    # sort genre_tot by value
    genre_tot = sorted(genre_tot.items(), key = lambda x: x[1], reverse = True)
    
    # sort each items of genre_dic by plays
    for item in genre_tot:
        playlist = genre_dic[item[0]]
        playlist = sorted(playlist, key = lambda x: x[0], reverse = True)
        for i in range(len(playlist)):
            if i==2:
                break
            answer.append(playlist[i][1])


    return answer

    