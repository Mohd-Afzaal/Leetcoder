class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        if n == 1:
            return True
        if n%2==0:
            while(2**power < n+1 ):
                if (2**power == n):
                    return True
                power+=1
        return False

# Alternative solution using bit manipulation
    def isPowerOfTwoBitManipulation(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0