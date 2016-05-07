class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        sign = 1
        sign_flag = False
        num_flag = False
        if str == '': return 0
        for s in str:
            if s >= '0' and s <='9':
                num_flag = True
                num = num*10 + ord(s) - ord('0')
            elif sign_flag or num_flag:
                break
            elif num == 0 and (s == '+' or s == '-'):
                sign_flag = True
                if s == '-': sign = -1
            elif s == ' ': 
                continue
            else:
                break
        
        num *= sign
        num = min(num, 2147483647)
        num = max(num, -2147483648)
            
        return num