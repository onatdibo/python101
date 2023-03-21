
x = 3

try:
    print(x) # executed this blog, because x = 3
except NameError:
    print("error x is not defined")


try:
    print(y)
except:
    print("error") # executed this blog, because x not defined

try:
    print(z)
except NameError: # NameError Triggered when trying to reach an undefined variable name
    print("error") # executed this blog

# coming soon...