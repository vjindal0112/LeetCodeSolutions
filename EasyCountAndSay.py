# Runtime: 32 ms, faster than 98.84% of Python3 online submissions for Count and Say
# Memory Usage: 13.7 MB, less than 6.38% of Python3 online submissions for Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        out = "11"
        if(n == 1):
            return "1"
        if(n == 2):
            return out

        for x in range(n-2):
            newOut = ""
            count = 1
            for k in range(1, len(out)+1):
                if(k == len(out)):
                    newOut += str(count) + out[k-1]
                else:
                    if(out[k] == out[k-1]):
                        count += 1
                    else:
                        newOut += str(count) + out[k-1]
                        count = 1
            print(newOut)
            out = newOut

        return out
