class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x1, x2):
        p1, p2, = self.find(x1), self.find(x2)
        if p1 == p2: return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))
        emailToAccIndex = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccIndex:
                    uf.union(i, emailToAccIndex[e])
                else: 
                    emailToAccIndex[e] = i

        emailGroup = defaultdict(list)
        for email, i in emailToAccIndex.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res