x = 3

try:
    print(x)  # executed this blog, because x = 3
except NameError:
    print("error x is not defined")


try:
    print(x)
except:
    print("error")  # executed this blog, because x not defined


try:
    print(x)
except NameError:  # NameError Triggered when trying to reach an undefined variable name
    print("error")  # executed this blog


try:
    print("Code True")
except:
    print("code false")
finally:
    print("No errors")  # true or false this part works


a = -1

# Raise an exception and TypeError

if a < 0:
  raise Exception("Sorry, no numbers below zero") # To throw (or raise) an exception, use the raise keyword.


b = "hello"

if not type(b) is int:
  raise TypeError("Only integers are allowed")