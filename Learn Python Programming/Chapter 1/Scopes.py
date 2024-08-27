#scope example 1
print("Example 1: both local and global variables")
def local1():
    a = 7
    print(a)
a = 5
local1()         # 7
print(a)        # 5

#scope example 2
print("EXAMPLE 2: global variable used locally")
def local2():
    print(b)
b=5
print(b)
local2()

#scope example 3
print("EXAMPLE 3: enclosing and global variable")
def enclosing():
    c = 10
    def local3():
        print(c)
    local3()
c = 20
print(c)
enclosing()
