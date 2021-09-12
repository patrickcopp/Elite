class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current, nums):
            if len(nums) == 0:
                res.append(current)
                return
            for i in nums:
                current.append(i)
                tmp = nums[::]
                tmp.remove(i)
                backtrack(current[:], tmp)
                current.pop()
        backtrack([],nums)
        return res