class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stack = []
        for el in path:
            if not el: pass
            elif el == '.': pass
            elif stack and el == '..': stack.pop()
            elif not stack and el == '..': pass
            else: stack.append(el)
        print(stack)
        return '/' + '/'.join(stack)
