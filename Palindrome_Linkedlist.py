class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            tem = slow.next
            slow.next = prev
            prev = slow
            slow = tem
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list (for debugging purposes)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test the isPalindrome function
values = [1, 2, 3, 2, 1]  # Example of a palindrome linked list
head = create_linked_list(values)
solution = Solution()
print("Is palindrome:", solution.isPalindrome(head))  # Expected output: True

values = [1, 2, 3, 4, 5]  # Example of a non-palindrome linked list
head = create_linked_list(values)
print("Is palindrome:", solution.isPalindrome(head))  # Expected output: False
