class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[pos, sp] for pos, sp in zip(position, speed)]
        pos_speed.sort(reverse=True)
        stack = []
        for el in pos_speed:
            time = (target - el[0])/el[1]
            if stack and time > stack[-1]:
                stack.append((target - el[0])/el[1])
            if not stack:
                stack.append((target - el[0])/el[1])
        return len(stack)