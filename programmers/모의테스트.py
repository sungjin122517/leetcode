user_input = input()
#split user_input by space
n, k = user_input.split()
# convert n, k from str to int
n = int(n)
k = int(k)

nums = input()
nums = nums.split()

# make list of integer from 1 to n
numsList = [i for i in range(1, n+1)]
kList = list(map(int, nums))

# sum up elements from numsList that are not in kList
ans = sum([i for i in numsList if i not in kList])


def solution():
    nAndK = input()
    n, k = nAndK.split()
    n = int(n)
    k = int(k)

    nums = input()
    nums = nums.split() # nums is already array
    # make elements of nums to integer
    numsList = list(map(int, nums))

    for i in range(k):
        xAndC = input()
        x, c = xAndC.split()
        x = int(x)
        c = int(c)

        if c == 0:
            numsList = [i for i in numsList if i < x]
        elif c == 1:
            numsList = [i for i in numsList if i > x]
    
    return len(numsList)

