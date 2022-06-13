#Leetcode
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def len_of_ll(head, counter=1):
            if not head.next:
                return counter
            else:
                temp_counter = len_of_ll(head.next, counter)
                counter += temp_counter
            return counter
        iter_limit = len_of_ll(head) -n
        if iter_limit ==0:
            return head.next
        curr_node = head
        counter = 0
        while counter < iter_limit-1:
            curr_node = curr_node.next
            counter +=1
        curr_node.next = curr_node.next.next
        return head
            
                
        