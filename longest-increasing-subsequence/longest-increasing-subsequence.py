class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = [1] * len(nums)
        longest[0] = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    longest[i] = max(longest[i], longest[j] + 1)
        return max(longest)