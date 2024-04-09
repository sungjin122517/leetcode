from typing import List

def sortArray(self, nums: List[int]) -> List[int]:

    def merge(arr, start, mid, end):
        L, R = arr[start:mid+1], arr[mid+1:end+1]
        i, j, k = start, 0, 0

        while j < len(L) and k < len(R):
            if L[j] <= R[k]:
                arr[i] = L[j]
                j += 1
            else:
                arr[i] = R[k]
                k += 1
            i += 1
        while j < len(L):
            arr[i] = L[j]
            j += 1
            i += 1
        while k < len(R):
            arr[i] = R[k]
            k += 1
            i += 1

    def mergeSort(arr, start, end):
        if start == end:
            return arr
        mid = (start+end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)
        return arr
    
    return mergeSort(nums, 0, len(nums)-1)
    
    


