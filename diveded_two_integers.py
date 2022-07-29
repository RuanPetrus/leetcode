class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1): return 2147483647

        quotient = 0
        dividend_sign = False
        divisor_sign = False

        if dividend < 0:
            dividend_sign = True
            dividend = 0 - dividend
        if divisor < 0:
            divisor_sign = True
            divisor = 0 - divisor

        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        if divisor_sign != dividend_sign:
            quotient = 0 - quotient

        if quotient > (2 ** 31 - 1):
            return (2 ** 31 - 1)
        elif quotient < (- (2 ** 31)):
            return (- (2 ** 31))

        return quotient


sol = Solution()
print(sol.divide(-2147483648, -1))
