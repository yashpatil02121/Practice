nums = [1,1,4,6,4,3,8,8]

def find_all_missing_numbers(nums):
    for i in range(len(nums)):
        temp = abs(nums[i])-1
        if nums[temp] > 0:
            nums[i] *= -1

        result = []


    for i,v in enumerate(nums):
        if v > 0:
            result.append(i+1)

    print(result)




find_all_missing_numbers(nums)