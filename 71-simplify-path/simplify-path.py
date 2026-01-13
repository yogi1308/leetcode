class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for el in path:
            if not el or el == '.' or not stack and el == '..': pass
            elif el == '..': stack.pop()
            else: stack.append(el)
        return '/' + '/'.join(stack)
