class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set(deadends)
        if "0000" in ends: return -1
        if "0000" == target: return 0
        q = deque()
        q.append(("0000", 0))
        visited = set()
        visited.add("0000")
        def algo(num, intstr, i):
            if intstr == "-1": intstr = "9"
            elif intstr == "10": intstr = "0"
            numCopy = num[0][:]
            numCopy = num[0][:i] + str(intstr) + num[0][i+1:]
            if numCopy == target: return num[1] + 1
            if numCopy not in visited and numCopy not in ends: 
                q.append((numCopy, num[1] + 1))
                visited.add(numCopy)

        def bfs(num):
            int1, int2, int3, int4 = int(num[0][0]), int(num[0][1]), int(num[0][2]), int(num[0][3])
            nums = [int1, int2, int3, int4]
            for i in range(len(nums)):
                for intstr in [str(nums[i] + 1), str(nums[i] - 1)]:
                    result = algo(num, intstr, i)  
                    if result is not None: return result

        while q:
            result = bfs(q.popleft())
            if result is not None: return result

        return -1