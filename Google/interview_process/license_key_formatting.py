# Fruit Into Baskets
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S or not K: return ''
        chars = ''.join(S.split('-'))[::-1]
        seperator = 0 
        license = []
        builder = ''
        for i in range(len(chars)):
            char = chars[i]
            seperator += 1
            builder += char
            if seperator == K or i == len(chars) - 1:
                license.append(builder[::-1])
                builder = ''
                seperator = 0
        return ('-'.join(license[::-1])).upper()