class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 0 -> 0 middle
        # 1 -> in between 0, 1
        # 2 -> 1 middle
        # 3 -> in between 1, 2
        
        def expansion(i1,i2):
            if i1 < 0 or i2 >= len(s) or s[i1] != s[i2]:
                return (i1 + 1, i2 - 1)
            return expansion(i1 - 1, i2 + 1)
        
        
        
        max_parts = (0,0)
        for i in range(2 * len(s) - 1):
            if i % 2 == 0:
                result = expansion(i//2, i//2)
            else:
                result = expansion(i//2, i//2 + 1)
                
            if result[1] - result[0] > max_parts[1]- max_parts[0]:
                max_parts = result
                    
        return s[max_parts[0]:max_parts[1] + 1]