class Solution:
    def reverse(self, x: int) -> int:

        MAX_INT = 2**31
        MIN_INT = -2**31
        reverse = 0

        while x != 0:
            if x >= 0:
                last_digit = x % 10
            else:
                last_digit = x % -10
            
            reverse = reverse*10 + last_digit
            if reverse > 2**31 or reverse <-2**31:
                return 0
            x = math.trunc(x/10)

        return reverse




        # if x >= 0:
        #     x = str(x)
        #     x = x[::-1]
        #     x = int(x)
        #     if x >2**31 or x < -2 **31:
        #         return 0
        #     return x
        # else:
        #     x = str(x)
        #     sign = x[0]
        #     x = x[1:]
        #     x = x[::-1]
        #     x = -1 * int(x)
        #     if x >2**31 or x < -2 **31:
        #         return 0
        #     return x

        