class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open, par, openedPar):
            if openedPar == n:
                for i in range(open):
                    par += ")"
                res.append(par[:])
                return
                
            if openedPar < n:
                par += "(" 
                dfs(open + 1, par, openedPar + 1)
                par = par[:-1]
                if open > 0:
                    par += ")"
                    dfs(open - 1, par, openedPar)
        dfs(0, "", 0)
        return res

