#Leetcode
#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def length_of_ll(node, counter=1):
            if not node:
                return 0
            if not node.next:
                return counter
            else:
                counter += length_of_ll(node.next)
            return counter
        result_ll = ListNode()
        len_1 = length_of_ll(list1)
        len_2 = length_of_ll(list2)
        list1_node = list1
        list2_node = list2
        list3_node = result_ll
        counter = 0
        while counter < len_1+len_2:
            temp_node = ListNode()
            if not list1_node:
                list3_node.next = list2_node
                break
            elif not list2_node:
                list3_node.next = list1_node
                break
            elif list1_node.val<list2_node.val:
                temp_node.val = list1_node.val
                list1_node = list1_node.next
                list3_node.next = temp_node
            elif list2_node.val<list1_node.val:
                temp_node.val = list2_node.val
                list2_node = list2_node.next
                list3_node.next = temp_node
            else:
                temp_node.val = list1_node.val
                list1_node = list1_node.next
                temp_node.next = ListNode(list2_node.val)
                list2_node = list2_node.next
                list3_node.next = temp_node
                list3_node = list3_node.next
            
            list3_node = list3_node.next
            counter += 1
        return result_ll.next
            
        
            
        