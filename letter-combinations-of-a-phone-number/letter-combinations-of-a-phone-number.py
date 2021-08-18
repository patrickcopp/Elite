class Solution:
    letters = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.letters[digits[0]]
        
        list_of_possibilities = []
        for i in self.letters[digits[0]]:
            self.recurse(digits[1:], list_of_possibilities, i)
            
        return list_of_possibilities
    
    def recurse(self, current_string, list_of_possibilities, builder):
        print(current_string)
        print(type(current_string))
        if len(current_string) == 1:
            for i in self.letters[current_string[0]]:
                list_of_possibilities.append(builder + i)
            return
        for i in self.letters[current_string[0]]:
            self.recurse(current_string[1:], list_of_possibilities, builder+i)