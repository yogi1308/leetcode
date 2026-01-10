class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            mag = abs(asteroid)
            direction = "+" if abs(asteroid) == asteroid else "-"
            while True:
                if stack:
                    prev_asteroid = stack[-1]
                    prev_ast_mag = abs(prev_asteroid)
                    prev_ast_dir = "+" if abs(prev_asteroid) == prev_asteroid else "-"
                    if direction == prev_ast_dir or (prev_ast_dir == "-" and direction == "+"): 
                        stack.append(asteroid)
                        break
                    if mag > prev_ast_mag:
                        stack.pop()
                    elif mag < prev_ast_mag:
                        break
                    elif mag == prev_ast_mag:
                        stack.pop()
                        break
                else:
                    stack.append(asteroid)
                    break
        return stack
