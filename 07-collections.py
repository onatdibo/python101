# 1- LIST

products = ["notebook", "book", "pencil"]
print(products)

# list items

print(products[2]) # output : "pencil"

# Changeable list

products.append("bag") # added new product
print(products)

# remove list

products.remove("bag") # removed item "bag"
print(products)


# change the prudcts 

products[2] = "keyboard" # Old : "keyboard"
print(products)


# 2- TUPPLES

fruits = ("apple", "banana", "cherry")
print(fruits)

print(len(fruits)) # To determine how many items a tuple has, use the len() function:

# access the tupple
print(fruits[1])

test = (1, True, "Hf", 2.4) #  tupples different data types
print(test)


test2 = tuple(("john", "adriana")) # created new tupple
print(test2)
