# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.int_to_list(self.list_to_int(l1) + self.list_to_int(l2))
        
        
                    
    def list_to_int(self, l1: Optional[ListNode]) -> int:
        number_string = ''
        
        while l1 is not None:
            number_string += str(l1.val)
            l1 = l1.next

        return int(number_string[::-1])

    def int_to_list(self, n: int) -> ListNode:
        number_string = str(n)
        previus = None
        current = None

        for i in number_string:
            current = ListNode(int(i), previus)
            previus = current

        return current


sol = Solution()

print(sol.countSubstrings("aaa"))
