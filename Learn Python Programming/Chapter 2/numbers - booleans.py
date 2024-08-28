# subset of algera where values are either True or False, subclass of Integers where True an False behaves like 1 and 0 respectively.
print("\n================================")
print(int(True)) # 1
print(int(False)) # 0
print(bool(1)) # True
print(bool(0)) # False
print(bool(-10)) # True 

# boolean values can be used combined with logical operations (and, or and not) in boolean expressions.

print("\n================================")
print(not True) # False
print(not False) # True

print("\n================================")
print(True and True) # True
print(True and False) # False
print(False and False) # False
print(False and True) # False

print("\n================================")
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print("\n================================")
print(f'{1 + True = }') # 2
print(f'{1 + False = }') # 1
print(f'{1 - True = }') # 0
print(f'{1 - False = }') # 1

print("\n================================")