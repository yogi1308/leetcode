class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        output = []
        shift = 1 if k >= 0 else -1
        for i in range(len(code)):
            sum_this = []
            for j in range(abs(k)):
                idx = (i + (j * shift) + shift) % len(code) if (i + (j * shift) + shift) >= len(code) else i + (j * shift) + shift
                sum_this.append(code[idx])
            output.append(sum(sum_this))
        return output
