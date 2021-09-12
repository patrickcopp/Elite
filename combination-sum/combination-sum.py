class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        memo = {} 
        def backtrack(target, index, current):
            if target == 0:
                res.append(list(current))
                return
            elif target < 0:
                return
            for i in range(index, n):
                current.append(candidates[i])
                backtrack(target - candidates[i], i, current)
                current.pop()
        backtrack(target, 0, [])
        return res