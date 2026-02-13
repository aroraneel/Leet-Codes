from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if prev == None:
            return None

        nxt = prev.next

        while nxt != None:
            if prev.val == nxt.val:
                prev.next = nxt.next
                nxt = nxt.next
            else:
                prev = nxt
                nxt = nxt.next

        return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    sol = Solution()

    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

    result = sol.deleteDuplicates(head)

    print("Linked List after removing duplicates:")
    printList(result)

    # Summary:
    # This program removes duplicates from a sorted linked list.
    # It compares each node with the next node.
    # If two consecutive nodes have the same value, the duplicate node is skipped.
    # The final linked list contains only unique values.
