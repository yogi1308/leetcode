class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        hmap = defaultdict(set)
        for n1, n2 in edges:
            hmap[n1].add(n2)
            hmap[n2].add(n1)

        def dfs(node, target, visited):
            if node == target: return True
            if node in visited: return False
            visited.add(node)
            for n in hmap[node]:
                if dfs(n, target, visited): return True
            return False

        for edge in reversed(edges):
            n1, n2 = edge
            hmap[n1].remove(n2)
            hmap[n2].remove(n1)
            if dfs(n1, n2, set()): return edge
            hmap[n1].add(n2)
            hmap[n2].add(n1)