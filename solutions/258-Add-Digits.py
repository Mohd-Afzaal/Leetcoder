class Solution:
    def addDigits(self, num: int) -> int:
        flag = True
        sum = 0
        while(flag):
            if num:
                sum+=num%10
                num//=10
            elif num == 0 and sum > 9:
                num,sum = sum, 0
            elif sum <= 9:
                flag = False
        return sum
    