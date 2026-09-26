# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlst = []
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            pointer1 = list1
            pointer2 = list2
            dummy = ListNode()
            dummyPointer = dummy
            while pointer1 and pointer2:
                if (pointer1.val <= pointer2.val):
                    dummyPointer.next = pointer1
                    pointer1 = pointer1.next
                else:
                    dummyPointer.next = pointer2
                    pointer2 = pointer2.next
                dummyPointer = dummyPointer.next
            if pointer1:
                dummyPointer.next = pointer1
            else:
                dummyPointer.next = pointer2
        return dummy.next

                    
            
