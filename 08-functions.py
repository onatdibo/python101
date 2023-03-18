# create function

def myFunction():
    print("Function1")
# call function
myFunction()

# usage parameters
def myFunction2(name):
    print("welcome", name)

myFunction2("Hesflay")

def myFunction3(say1, say2):
    print("Total:", say1 + say2)
myFunction3(10, 20)

# Arbitrary Arguments, *args

def myFuction4(*fruits):
    print("The name of the fruit", fruits[2])
myFuction4("apple", "banana", "cherry")


# Keyword Arguments
# You can also send arguments with the key = value syntax.

def myFunction5(child1, child2, child3):
    print("chid is", child2)
myFunction5(child1="john", child2="edward", child3="alex")

# Default Parameter Value

def myFunction6(country = "Turkey"):
    print("I'm from", country)
myFunction6("Russia")
myFunction6("China")
myFunction6()

# return values

def myFunction7(x):
    return 5 * x

print( myFunction7(3) )
print( myFunction7(6) )
print( myFunction7(4) )

