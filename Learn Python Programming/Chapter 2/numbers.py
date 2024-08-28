# integers (positive, negative or zero of unlimited length as long as it fits in your computer memory)

a = 10
b = 3

print(f'{a + b = }') # 13, addition
print(f'{a - b = }') # 7, subtraction
print(f'{a * b = }') # 30, multiplication
print(f'{a / b = }') # 3.333333333333, division
print(f'{a // b = }') # 3, integer division
print(f'{a % b = }') # 1, modulo operation(finding remainder)
print(f'{a ** b = }') # 1000, power operation (a^b)

# for negative numbers:
print(f'{-7 / 4 = }') # -1.75, result is same, sign opposite
print(f'{-7 // 4 = }') # -2, not -1, integer division in Py always rounded towards minus infinitely

#truncation is done towards 0 and can be done using build-in int() function
print(f'{int(1.85) = }') #1, result is same, sign opposite
print(f'{int(-1.85) = }') #-1, similar to flooring