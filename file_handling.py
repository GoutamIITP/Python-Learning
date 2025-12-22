# File Handling 
# open(filename, mode) - Opens a file and returns a file object
# Modes: 'r' - read, 'w' - write, 'a' - append, 'b' - binary, 't' - text, 'x' - create
# read() - Reads the entire file

# Example of File Handling in Python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a file handling example in Python.\n')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)              

# Appending to a file
with open('example.txt', 'a') as file:
    file.write('Appending a new line to the file.\n')           
# Reading the updated file
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print(updated_content)      