"                           Shree Krishnaya Namaha              "

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print(self):
        node = self
        out_str = ""
        while node.next is not None:
            out_str += str(node.val) + "->"
            node = node.next
        out_str += str(node.val)

        print(out_str)

    # Iterative solution
    def reverseIteratively(self, head):
        cur_node = head
        prev_node = head

        if cur_node is None or cur_node.next is None:
            return cur_node
        
        prev_node = cur_node
        cur_node = cur_node.next
        prev_node.next = None

        while cur_node:
            temp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp

        head = prev_node
        return head

    def reverseRecursively(self, head):
        def rev_list_helper(node):
            global rev_head
            if node.next is None:
                rev_head = node
                return node
            elif node is None:
                return None
            else:
                temp = rev_list_helper(node.next)
                temp.next = node
                if node is head:
                    node.next = None
                return node
        rev_list_helper(head)
        return rev_head



list1 = ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0)))))
list1.print()
#list2 = list1.reverseIteratively(list1)
list2 = list1.reverseRecursively(list1)
list2.print()