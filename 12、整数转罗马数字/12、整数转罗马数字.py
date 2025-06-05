class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        lis = []
        pos = 1
        while num:
            v = num % 10
            num //= 10
            val = v * pos
            if val in dic:
                lis.append(dic[val])
            else:
                if v > 5:
                    lis.append(dic[5 * pos] + (v - 5) * dic[pos])
                else:
                    lis.append(v * dic[pos])
            pos *= 10
        return ''.join(lis[::-1])
