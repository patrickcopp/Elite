class TrieNode:
    def __init__(self, val = None, word = False):
        self.val = val
        self.word = word
        self.leafs = collections.defaultdict(TrieNode)
        
    def __repr__(self):
        return str(self.val)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.yup = False

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.leafs[w]
        node.word = True

    def search(self, word: str) -> bool:
        
        def dfs(root, word):
            if not word:
                if root.word:
                    self.yup = True
                return
            if word[0] == '.':
                for i in root.leafs.values():
                    dfs(i, word[1:])
            else:
                if word[0] not in root.leafs:
                    return
                root = root.leafs[word[0]]
                if not root:
                    return
                dfs(root, word[1:])
        
        self.yup = False
        root_copy = self.root
        dfs(root_copy, word)
        return self.yup


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)