class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = before = ListNode(0)
        carry = 0
        while  l1 is not None or l2 is not None or carry is not 0:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            carry, value = divmod(val1 + val2 + carry, 10)
            before.next = ListNode(value)
            before = before.next

        return head.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    while l3 is not None:
        print(l3.val)
        l3 = l3.next


