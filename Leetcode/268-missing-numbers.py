# nums = [3,0,1]
nums = [0,1]



# Slow Solution
# def missing_numbers(nums):
#     nums.sort()

#     for i,v in enumerate(nums):
#         # check if index and value matches if not, we found the missing number
#         if i != v:
#             print(v-1)
#             return v-1
#         # if all the numbers matches the index, then the last number is missing
#         if v == len(nums)-1:
#             print(v+1)
#             return v+1


def missing_numbers(nums):
    return sum(range(len(nums)+1))-sum(nums)


# explanation
# len(nums) + 1

# This gives the total count of numbers that should be there (including the missing one).

# Example: If nums = [0, 1, 3], then len(nums) = 3, and len(nums)+1 = 4.
# That means the full list should be: [0, 1, 2, 3]

# sum(range(len(nums)+1))

# This adds up all numbers from 0 to n (inclusive).

# Example: sum(range(4)) = 0 + 1 + 2 + 3 = 6

# sum(nums)

# This adds up the numbers in the given list.

# Example: sum([0, 1, 3]) = 4

# Subtract the two sums:

# 6 - 4 = 2 → That’s the missing number!




missing_numbers(nums)