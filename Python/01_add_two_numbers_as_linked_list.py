"                       Shree Krishnaya Namaha                  "

import sys
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    result = None
    carry = 0
    temp = None

    while l1 is not None or l2 is not None:
        cur_sum = 0
        if l1:
            cur_sum = l1.val
            l1 = l1.next
        if l2:
            cur_sum += l2.val
            l2 = l2.next

        cur_sum += carry
        carry = cur_sum // 10
        res = cur_sum % 10

        if result:
            temp.next = ListNode(res)
            temp = temp.next
        else:
            result = ListNode(res)
            temp = result

    if carry != 0:
        temp.next = ListNode(1)

    return result 

class SecondSolution:
  def addTwoNumbers(self, l1, l2, c = 0):
    num1 = 0
    num2 = 0

    mul = 1
    while l1 is not None:
        num1 = num1 + l1.val * mul
        mul = mul * 10
        l1 = l1.next
    
    mul = 1
    while l2 is not None:
        num2 = num2 + l2.val * mul
        mul = mul * 10
        l2 = l2.next
    sum_of_two = num1 + num2
    result_list = None
    return_list = None

    if sum_of_two == 0:
        return ListNode(0)
    while sum_of_two > 0:
        lsb = sum_of_two % 10
        sum_of_two = sum_of_two // 10
        if result_list:
            result_list.next = ListNode(lsb)
            result_list = result_list.next
        else:
            result_list = ListNode(lsb)
            return_list = result_list

    return return_list

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    sys.stdout.write(str(result.val))
    result = result.next
print ("")
l1 = ListNode(9)
l1.next = ListNode(9)

l2 = ListNode(1)


result = SecondSolution().addTwoNumbers(l1, l2)
while result:
    sys.stdout.write(str(result.val))
    result = result.next