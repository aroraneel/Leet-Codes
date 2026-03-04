from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == "__main__":
    sol = Solution()

    nums = [3, 2, 3]
    result = sol.majorityElement(nums)

    print("Array:", nums)
    print("Majority Element:", result)

    # Summary:
    # This program finds the majority element in an array.
    # A majority element appears more than n/2 times.
    # It uses Counter to count the frequency of each element.
    # The element with the highest frequency is returned.