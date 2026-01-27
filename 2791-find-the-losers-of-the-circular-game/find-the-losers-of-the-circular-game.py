class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        pass_count = 1
        not_passed = [i for i in range(1, n + 1)]
        curr = 1
        length = len(not_passed)
        while curr in not_passed:
            
            not_passed.remove(curr)
            if curr + (pass_count * k) <= length:
                curr += (pass_count * k)
            else:
                print("exec", (curr + (pass_count*k)) % length, pass_count*k)
                curr = (curr + (pass_count*k)) % length
            pass_count += 1
            if curr == 0: curr = n
            print(curr)
        return not_passed