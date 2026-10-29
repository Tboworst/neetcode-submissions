# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2


        return dummy.next
   

'''
Input:Lst1-> head of the first linked list(rememeber the heads leads you to everything)
list2 -> samething but of the 2nd list

Goal:Merge the two linkedin list into one and return the new SORTED linked list

Brute force:
Put the nodes data into an array sort the array
put the data back inot a linkedList

Return that


Optimal approach:

create a dummy node that points to head on list 1 and
2

traverse and create a linked list from that:

dummy =list1.head= list2.head

while head is not None:





'''
        

        
        