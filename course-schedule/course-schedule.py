from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = {}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        def dfs(current):
            if current in visited and visited[current]:
                return False
            if current not in adj or adj[current] == []:
                return True
            visited[current] = True
            for i in adj[current]:
                if not dfs(i):
                    return False
            visited[current] = False
            adj[current] = []
            return True
        
        for i in adj.keys():
            if not dfs(i):
                return False
        return True
        
        