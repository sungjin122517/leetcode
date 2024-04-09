# insertion sort, O(n^2)
def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, 0, -1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break

# selection sort, O(n^2)
def selection(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

# quick sort, O(nlogn)
def quick(arr):
    quick2(arr, 0, len(arr)-1)

def quick2(arr, low, high):
    if low < high:
        # get pivot position
        p = partition(arr, low, high)
        quick2(arr, low, p-1)
        quick2(arr, p+1, high)

def partition(arr, low, high):
    pivotIndex = getPivot(arr, low, high)
    pivotValue = arr[pivotIndex]
    # put pivot value at the beginning
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low

    for i in range(low, high+1):
        if arr[i] < pivotValue:
            arr[i], arr[border] = arr[border], arr[i]
            border += 1
    arr[low], arr[border] = arr[border], arr[low]

    return border

def getPivot(arr, low, high):
    mid = (high+low)/2
    pivot = high
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            pivot = mid
    elif arr[low] < arr[high]:
        pivot = low
    return pivot

# merge sort, O(nlogn)
def mergeSort(arr):
    mergeSort2(arr, 0, len(arr)-1)

def mergeSort2(arr, first, last):
    mid = (first+last)/2
    mergeSort2(arr, first, mid)
    mergeSort2(arr, mid+1, last)
    merge(arr, first, mid, last)

def merge(arr, first, mid, last):
    left = arr[first:mid]
    right = arr[mid+1:last+1]
    left.append(999999)
    right.append(999999)
    i = j = 0

    for k in range(first, last+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

# binary search, O(log n)
def binarySearch(nums: List[int], target: int):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid+1
        elif nums[mid] > target:
            r = mid-1
        else:
            return mid
    
    return -1