from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n = len(nums1) - m
        for i in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    sol.merge(nums1, m, nums2, n)

    print("Merged Array:", nums1)

    # Summary:
    # This program merges two sorted arrays into nums1 in-place.
    # It removes the extra placeholder zeros from nums1 using pop().
    # Then it adds all elements of nums2 into nums1 and sorts the final array.
    