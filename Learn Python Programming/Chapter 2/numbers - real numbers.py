# real number, or floating point numbers in Python are represented according to IEEE 754 double-precision binary floating point format i.e. store in 64 bits of info divided into three parts: sign, exponent and mantissa.
# "sys.float_info" holds info about how floating point numbers will behave on your system.

import sys

def real_number():
    print(sys.float_info)
    print("================================\n")

real_number()

# double precision real numbers suffers from floating point precision issues (approximation issues).
def approximation_issue():
    print(f'{0.3 - 0.1*3 = }')
    print("================================\n")

approximation_issue()

