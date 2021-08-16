class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        newDict = {}
        for i in wordDict:
            newDict[i] = True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in newDict:
                    dp[i] = True
                    break
        return dp[-1]