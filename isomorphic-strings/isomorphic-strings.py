class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        ok = set()
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in ok:
                    return False
                dic[s[i]] = t[i]
                ok.add(t[i])
            elif dic[s[i]] != t[i]:
                return False
            
        return True