nums = [4,3,2,7,8,2,3,1]

def find_all_missing(nums):
    set_nums = set(nums)

    result = []

    for i in range(1, len(nums)+1):
        if i not in set_nums:
            result.append(i)

    print(result)

def find_all_missing_enhanced(nums):

    for i in range(len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1
        # print(nums[temp])

    result = []
    for i,n in enumerate(nums):
        if n > 0:
            result.append(i+1)
    print(result)

find_all_missing(nums)
find_all_missing_enhanced(nums)








# Explanation

# 🧩 Initial Array:

# Index:   0   1   2   3   4   5   6   7
# Value:  [4,  3,  2,  7,  8,  2,  3,  1]
# 👉 Looping and marking:
# i = 0: nums[0] = 4
# → Mark index 3 → nums[3] = 7 becomes -7


# [4, 3, 2, -7, 8, 2, 3, 1]
# i = 1: nums[1] = 3
# → Mark index 2 → nums[2] = 2 becomes -2


# [4, 3, -2, -7, 8, 2, 3, 1]
# i = 2: nums[2] = -2 → abs(-2) = 2
# → Mark index 1 → nums[1] = 3 becomes -3


# [4, -3, -2, -7, 8, 2, 3, 1]
# i = 3: nums[3] = -7 → abs(-7) = 7
# → Mark index 6 → nums[6] = 3 becomes -3


# [4, -3, -2, -7, 8, 2, -3, 1]
# i = 4: nums[4] = 8
# → Mark index 7 → nums[7] = 1 becomes -1


# [4, -3, -2, -7, 8, 2, -3, -1]
# i = 5: nums[5] = 2
# → Mark index 1 → Already -3, so we skip

# i = 6: nums[6] = -3
# → Mark index 2 → Already -2, so we skip

# i = 7: nums[7] = -1
# → Mark index 0 → nums[0] = 4 becomes -4

# css

# [-4, -3, -2, -7, 8, 2, -3, -1]
# 🎉 After the first loop, array looks like:
# css

# [-4, -3, -2, -7, 8, 2, -3, -1]
# Negative = Seen
# Positive = Not Seen

# 🔁 Step 2: Finding Missing Numbers
# We now check which numbers are still positive.

# Indexes and values:
# makefile

# Index:   0   1   2   3   4   5   6   7
# Value: [-4, -3, -2, -7,  8,  2, -3, -1]
# Index 4 → value = 8 → still positive → 5 is missing

# Index 5 → value = 2 → still positive → 6 is missing

# ✅ So, missing numbers are: [5, 6]

# 📤 Final Output:
# python

# print(result)  # [5, 6]