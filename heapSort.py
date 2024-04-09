def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def heapify(list, i, max):
    while (i < max):
        # indices of left and right children
        left = 2 * i + 1    
        right = 2 * i + 2

        # find the largest of the three values
        largest = i
        if left <= max and list[left] > list[largest]:
            largest = left
        if right <= max and list[right] > list[largest]:
            largest = right
        if largest == i:
            break

        # swap with the largest child
        swap(list, i, largest)
        # continue heapifying down the tree
        i = largest

def heapsort(list):
    i = len(list) // 2 - 1
    i = int(i)

    # build a max heap
    while i >= 0:
        heapify(list, i, len(list) - 1)
        i -= 1

import heapq

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)

heapq.heappop(heap)

# 기존 리스트를 힙으로 변환
a_list = [4, 1, 7, 3, 8, 5]
heapq.heapify(a_list)
