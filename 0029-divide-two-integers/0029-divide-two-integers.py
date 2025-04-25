class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        k=0
        i=0
        f=0
        if dividend==divisor:
            return 1
        if dividend<0 and divisor>0:
            f=1
            if divisor==1:
                return dividend
            dividend=dividend-dividend-dividend
            if dividend==divisor:
                return -1
            
        if dividend>0 and divisor<0:
            f=1
            divisor=divisor-divisor-divisor
            if dividend==divisor:
                return -1
            if divisor==1:
                return dividend-dividend-dividend
        if dividend<0 and divisor<0:
            dividend=dividend-dividend-dividend
            divisor=divisor-divisor-divisor
            if divisor==1:
                return dividend-1
        if divisor==1:
            return dividend
        while dividend >= divisor:
            p = 0
            while dividend >= (divisor << p):
                p += 1
            
            p -= 1
            dividend -= (divisor << p)
            i += (1 << p)
        print(f,i)
        if f==1:
            return i-1-i+1-i
        return i