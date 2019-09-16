"                               Shree Krishnaya Namaha               "

def check(lst):
    num_of_misplaces = 0

    if not lst:
        return False

    prev_num = lst[0]

    for num in lst[1:]:
        if num > prev_num:
            num_of_misplaces += 1

        if num_of_misplaces > 1:
            return False
        prev_num = num

    return True

print (check([14, 4, 7]))
print (check([5,1,3,2,5]))