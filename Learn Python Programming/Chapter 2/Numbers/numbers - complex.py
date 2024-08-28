# Python supports complex numbers out of the box. 

def complex_number():
    a = 3 + 4j
    b = complex(3, 4)
    print(f'{a.real = }, {a.imag = }') # 3.0, 4.0
    print(f'{b.real = }, {b.imag = }') # 3.0, 4.0
    print(f'{a + b = }') # (6 + 8j)
    print(f'{a - b = }') # 0 
    print(f'{a * b = }') # (-7 + 24j), note that j=(-1)^2, therefore j^2 = -1
    print(f'{a / b = }') # (1 + 0j)
    print(f'|a| = {abs(a)}') # 5.0
    print(f'conjugate of a = {a.conjugate()}') # (3 - 4j), conjugate is a + bj -> a - bj
    print(f'a raised to power b = {a ** b}')

complex_number()