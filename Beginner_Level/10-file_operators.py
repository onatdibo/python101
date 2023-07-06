# https://www.w3schools.com/python/python_file_handling.asp


# read file
x = open("read.txt", "r") # "r" = read


print(x.read()) # reads the text inside

# write file

y = open("write.txt", "w") # "w" = write

y.write("Hesflay ") # prints it into the file


# create file

z = open("newFile.txt", "x") # "x" = create

z.write("Created new file.")

z.close()