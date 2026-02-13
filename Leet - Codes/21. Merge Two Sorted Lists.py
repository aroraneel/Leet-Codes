from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    sol = Solution()

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    result = sol.mergeTwoLists(list1, list2)

    print("Merged List:")
    printList(result)

    # Summary:
    # This program merges two sorted linked lists into one sorted linked list.
    # It uses a dummy node to simplify handling the merged list.
    # The smaller node from either list is chosen each time and added to the result.
    # Finally, any remaining nodes are attached, and the merged list is returned.
