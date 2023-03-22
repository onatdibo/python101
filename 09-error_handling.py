x = 3

try:
    print(x)  # executed this blog, because x = 3
except NameError:
    print("error x is not defined")


try:
    print(y)
except:
    print("error")  # executed this blog, because x not defined


try:
    print(z)
except NameError:  # NameError Triggered when trying to reach an undefined variable name
    print("error")  # executed this blog


try:
    print("Code True")
except:
    print("code false")
finally:
    print("No errors")  # true or false this part works


a = -1

# Raise an exception

if a < 0:
  raise Exception("Sorry, no numbers below zero") # To throw (or raise) an exception, use the raise keyword.