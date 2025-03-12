def romanToInt( s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i+1 < len(s) and roman_values[s[i]]<roman_values[s[i+1]]:
                total -=  roman_values[s[i]]
            else:
                total +=  roman_values[s[i]]
        return total


def int_to_roman(num):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman_numeral = ""

    for value, symbol in roman_map:
        while num >= value:
            roman_numeral += symbol
            num -= value

    return print(roman_numeral)


print(romanToInt("MMCM"))
int_to_roman(55)