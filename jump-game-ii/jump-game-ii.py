class Solution:
    def jump(self, nums: List[int]) -> int:
        reach=0
        mx=0
        jmp=0
        for i in range(len(nums)-1):
            mx = max(mx, i + nums[i])
            if i==reach:
                jmp+=1
                reach=mx
        return jmp
        