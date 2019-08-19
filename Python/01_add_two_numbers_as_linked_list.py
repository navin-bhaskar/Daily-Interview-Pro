"                       Shree Krishnaya Namaha                  "

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    result = None
    carry = 0
    temp = None

    while l1 is not None and l2 is not None:
        cur_sum = l1.val + l2.val + carry
        carry = cur_sum // 10
        res = cur_sum % 10
        if result:
            temp.next = ListNode(res)
            temp = temp.next
        else:
            result = ListNode(res)
            temp = result

        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        cur_sum = l1.val + carry
        res = cur_sum % 10
        carry = cur_sum // 10
        if result:
            temp.next = ListNode(res)
            temp = temp.next
        else:
            result = ListNode(res)
        l1 = l1.next

    while l2 is not None:
        cur_sum = l2.val + carry
        res = cur_sum % 10
        carry = cur_sum // 10
        if result:
            temp.next = ListNode(res)
            temp = temp.next
        else:
            result = ListNode(res)
        l2 = l2.next

    if carry != 0:
        temp.next = ListNode(1)

    return result 

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# result = Solution().addTwoNumbers(l1, l2)
# while result:
#     print (result.val),
#     result = result.next

l1 = ListNode(9)
l1.next = ListNode(9)

l2 = ListNode(1)


result = Solution().addTwoNumbers(l1, l2)
while result:
    print (result.val),
    result = result.next