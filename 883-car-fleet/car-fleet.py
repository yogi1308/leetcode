class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[pos, sp] for pos, sp in zip(position, speed)]
        pos_speed.sort(reverse=True)
        fleet = 0
        prev_time = 0
        for p, s in pos_speed:
            time = (target - p) /s
            if prev_time == 0 or time > prev_time:
                fleet += 1
                prev_time = (target - p) /s
        return fleet