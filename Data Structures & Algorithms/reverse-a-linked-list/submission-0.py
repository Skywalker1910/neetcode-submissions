# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            # 1.Save the next node
            next_node = current.next

            # 2. Reverse the current nodes pointer
            current.next = prev
            
            #3. Advance prev
            prev = current

            #4. Advance current
            current = next_node
        
        
        return prev