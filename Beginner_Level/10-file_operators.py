# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists



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