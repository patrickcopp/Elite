from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        mydict = set(wordList)
        
        queue = deque()
        queue.append(beginWord)
        depth = 0
        while len(queue) != 0:
            depth += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    tmp = word
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = tmp[:i]+j+tmp[i + 1:]
                        if tmp == word:
                            continue
                        if tmp == endWord:
                            return depth + 1
                        if tmp in mydict:
                            queue.append(tmp)
                            mydict.remove(tmp)
        return 0