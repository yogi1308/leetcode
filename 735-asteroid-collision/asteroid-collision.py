class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                curr_mag = abs(asteroid)
                prev_ast = stack[-1]
                if curr_mag > prev_ast:
                    stack.pop()
                elif curr_mag == prev_ast:
                    stack.pop()
                    break
                elif curr_mag < prev_ast:
                    break
            else:
                stack.append(asteroid)
        return stack
