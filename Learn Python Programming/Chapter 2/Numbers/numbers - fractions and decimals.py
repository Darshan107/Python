# Fractions hold a rational numerator and denominator in their lowest forms. 

from fractions import Fraction

def practice_fraction():
    print(f'{Fraction(10,6) = }') # Fraction(5, 3), reduced to lowest term
    print(f'{Fraction(1,3) + Fraction(2,3) =}') # Fraction(1, 1), 1/3 + 2/3 = 1/1 
    f = Fraction(10,6)
    print(f'{f.numerator, f.denominator = }') # (5, 3)
    print(f.as_integer_ratio()) # (5,3)
    print("================================\n")

practice_fraction()


# Decimals are used in all contexts for using fraction where precision is everything. 

from decimal import Decimal as D # renamed Decimal to D

def practice_decimal():
    print(f'{D(3.14) = }') # approximation issue for floats
    print(f'{D("3.14") = }') # no such issue for strings
    print(f'{D(0.1)*D(3)-D(0.3) = }')
    print(f'{D("0.1")*D("3")-D("0.3") = }')
    print(f'{D("1.4").as_integer_ratio() = }') # (7, 5)
    print("================================\n")

practice_decimal()