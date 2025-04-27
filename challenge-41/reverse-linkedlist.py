# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        temp = head
        while temp:
            ls.append(temp.val)
            temp = temp.next
        temp = head
        n = len(ls)-1
        while temp:
            temp.val = ls[n]
            n-=1
            temp = temp.next
        return head

        
        