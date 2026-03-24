from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, nxt = None, None
        curr = head

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    sol = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    result = sol.reverseList(head)

    print("Reversed Linked List:")
    printList(result)

    # Summary:
    # This program reverses a singly linked list.
    # It uses three pointers: prev, curr, and next.
    # Each node’s next pointer is reversed one by one.
    # Finally, prev becomes the new head of the reversed list.