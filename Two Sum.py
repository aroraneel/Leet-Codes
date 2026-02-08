class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# -------- Main Program --------
if __name__ == "__main__":
    nums = [2, 4, 6, 1]
    target = 3   # ✅ 2 + 1 = 3

    sol = Solution()
    result = sol.twoSum(nums, target)

    print("Array:", nums)
    print("Target:", target)
    print("Indexes:", result)
