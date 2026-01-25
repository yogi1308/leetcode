class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        output = []
        if k >= 0:
            for i in range(len(code)):
                sum_this = []
                for j in range(k):
                    idx = (i + j + 1) % len(code) if (i + j + 1) >= len(code) else i + j +1
                    sum_this.append(code[idx])
                output.append(sum(sum_this))
        else:
            for i in range(len(code)):
                sum_this = []
                for j in range(abs(k)):
                    idx = (i - j - 1) % len(code) if (i - j - 1) >= len(code) else (i - j -1)
                    sum_this.append(code[idx])
                print(sum_this)
                output.append(sum(sum_this))
        return output
