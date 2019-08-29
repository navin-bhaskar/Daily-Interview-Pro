"                       Shree Krishnaya Namaha                      "
def singleNumber(nums):
    accumalator = 0

    for num in nums:
        accumalator = accumalator ^ num

    return accumalator

print (singleNumber([4, 3, 2, 4, 1, 3, 2]))
assert (1 == singleNumber([4, 3, 2, 4, 1, 3, 2]))
assert (2 == singleNumber([1, 1, 5, 2, 4, 4, 5]))
assert (3 == singleNumber([4, 3, 2, 4, 1, 1, 2]))
assert (4 == singleNumber([4, 3, 2, 1, 1, 3, 2]))