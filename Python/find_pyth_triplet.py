"""
Find the Pythogrean triplet in a given list.
"""

def findPythagoreanTriplets(nums):
    """
    Find the Pythogrean triplet using a Hash map
    """
    cache = dict()

    for i in range(len(nums)):
        temp = nums[i]^2
        cache[temp] = i

    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue
            a = nums[i]^2
            b = nums[j]^2
            posiblity_one = abs(1-b)
            posiblity_two = a + b
            if posiblity_one in cache:
                if cache[posiblity_one] != i or cache[posiblity_one] != j:
                    return True
            if posiblity_two in cache:
                if cache[posiblity_two] != i or cache[posiblity_two] != j:
                    return True


    return False

assert (True == findPythagoreanTriplets([3, 12, 5, 13]))
assert (False == findPythagoreanTriplets([3, 13, 6, 13]))
