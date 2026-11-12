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
Create a new list:
dummy = listNode()
#set dummy to the head not a specificed list


Both of the linked list have heads


Check if the linked lists heads are valid

if list1 < list2:
    dummy = list1


The idea visualized

L1 1->2->3

l2 1->3->4

Compared the nodes if node in list 1 < list2:
add it and move in the list only -> vice versa is aother until you move to end 

If no more value in one of the list is empty but we have more
add that list to the end


    



'''
        