class Solution:
    def removeElement(self, nums, val):
        write = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1

        return write


if __name__ == "__main__":
    sol = Solution()

    nums = [3, 2, 2, 3, 4, 3]
    val = 3

    k = sol.removeElement(nums, val)

    print("Array after removing element:", nums[:k])
    print("Number of remaining elements:", k)

    # Summary:
    # This program removes all occurrences of a given value from the array in-place.
    # It uses a write pointer to overwrite unwanted elements.
    # The function returns the count of elements that are not equal to the given value.
