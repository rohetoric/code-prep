class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x >2**31 or x < -2 **31:
                return 0
            return x
        else:
            x = str(x)
            sign = x[0]
            x = x[1:]
            x = x[::-1]
            x = -1 * int(x)
            if x >2**31 or x < -2 **31:
                return 0
            return x

        