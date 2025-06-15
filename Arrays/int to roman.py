roman_map = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
num = 49
result = []
for value,symbol in roman_map:
    count = num // value
    result.append(symbol*count)
    num = num - (value*count)
print("".join(result))
