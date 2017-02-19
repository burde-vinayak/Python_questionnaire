def min3(num1, num2, num3):
    return num1 if num1<=num2 and num1<=num3 else num2 if num2 <= num1 and num2 <= num3 else num3

print min3(1, 2, 3)
print min3(3, 2, 1)
print min3(1, 3, 2)