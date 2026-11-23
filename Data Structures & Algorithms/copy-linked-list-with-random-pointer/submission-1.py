"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_to_new = {None: None}

        current = head

        while current is not None:
            new_node = Node(current.val)

            old_to_new[current] = new_node

            current = current.next

        current = head

        while current is not None:
             copy = old_to_new[current]

             copy.next = old_to_new[current.next]
             copy.random = old_to_new[current.random]

             current = current.next
             
        return old_to_new[head]
