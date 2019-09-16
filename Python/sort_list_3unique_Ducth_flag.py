"                       Shree Krishnaya Namaha                  "

def sortNums(nums):
    """
    Sort a list with 3 unique numbers using Dutch flag algo.
    Time complexity: O(n)
    Space complexity: O(1)

    We maintian three pointers, low, high and mid.
    low points to the correct location(s) for least of three values 1 in this case
    mid points to the correct location(s) for value > low and value < high, 2 in this case
    high points to the correct location(s) for highest of three numbers

    Start with low=mid=0
    We increment the low and mid once we have a found right places for 1 and 2
    Decrement high on putting the high value in one of the right indices

    Here the 2 is considered as pivot and then 
    """
    low = 0
    mid = 0
    high = len(nums) - 1
    pivot = 2

    while mid <= high:
        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1    # 'mid'has not reachead the actual mid yet
        elif nums[mid] == pivot:
            mid += 1   # NO swapping we are in middle
        elif nums[mid] > pivot:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1 # We want to stop 'mid' at the middle of sorted list so do not touch this ptr
    return nums

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
