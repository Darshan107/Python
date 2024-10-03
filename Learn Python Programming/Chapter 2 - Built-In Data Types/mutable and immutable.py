age = 42
age = 43
# these may seem like we can change integers but, 

hello = 10
print(id(hello))
hello = 40
print(id(hello))
# both id's will be different proving that they are different object
# what happens is that when we define name = value, a object (with its unique id, suitable type, and value given) is created and the name actually points to that object.
# reassigning the name to something else creates a new object which the name points to.

# here is an example of mutable data type
class Person(object):
    def __init__(self,age):
        self.age = age
fab = Person(age = 24)
print(fab.age)
print(f"{id(fab) = }, {id(fab.age) = }")
fab.age = 40
print(f"{id(fab) = }, {id(fab.age) = }")

#fab being an object, is mutable and its id dont change while fab.age only changes its id
defghi