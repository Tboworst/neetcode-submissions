# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        dummy = ListNode()
        dummy.next= head
        slow = fast= dummy

        while fast and fast.next:
            fast = fast.next.next

            slow = slow.next

            if slow is fast:
                return True

        return False


'''
Head: Links us to all the ndoes in the linked list

Goal: Return True is there is a cycle in the list,false otherwise

A cycle: when an index can be visted again by following the next pointer


'''