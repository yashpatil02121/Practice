# input = [1,4,3,6,7,0]
# output = 42


def maximum_product(arr):
    if len(arr) > 1:
        arr.sort()
        arr.reverse()
        print(arr[0]*arr[1])

arr = [1,4,3,6,7,0]

maximum_product(arr)