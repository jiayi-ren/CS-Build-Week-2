# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        carry = 0
        temp = ans
        while l1 or l2 :
            # print(ans)
            # if l1: print("l1 ",l1.val)
            # if l2: print("l2 ",l2.val)
            v1 = l1.val if l1 != None else 0
            v2 = l2.val if l2 != None else 0
            
            summ = v1 + v2 + carry
            carry = int(summ /10)

            temp.next = ListNode(summ%10)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            temp.next = ListNode(carry)
            
        return ans.next