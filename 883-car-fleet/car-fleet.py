class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(pos, sp) for pos, sp in zip(position, speed)]
        pos_speed.sort(reverse=True)
        fleet = 0
        prev_time = 0
        for el in pos_speed:
            time = (target - el[0]) /el[1]
            if prev_time == 0 or time > prev_time:
                fleet += 1
                prev_time = time
        return fleet