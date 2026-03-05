from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode()
        node.next = head
        temp = node

        while temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return node.next


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    sol = Solution()

    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(6)))))
    val = 6

    result = sol.removeElements(head, val)

    print("Linked List after removing", val, ":")
    printList(result)

    # Summary:
    # This program removes all nodes from a linked list that have a specific value.
    # A dummy node is used to handle edge cases like removing the head node.
    # The list is traversed and nodes with the given value are skipped.
    # The modified linked list is returned.