target = 9
nums = [2, 11, 15, 7]

# brute force
# nesting 2 loops - slow soluiton



# Use Hash Maps 
# Also called Dictionary in Python 


def two_sum(nums):
    hash_map = {} # val, index

    for i,v in enumerate(nums):
        if target - v in hash_map:
            # print(hash_map)
            return i, hash_map[target-v]
        else:
            hash_map[v] = i

print(two_sum(nums))