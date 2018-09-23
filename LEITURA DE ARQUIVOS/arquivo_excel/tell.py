#!/usr/bin/python

# Open a file
fow = open("foo.txt", "w")
print("Name of the file: ", fow.name)

fo = open("foo.txt", "r")
# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print("Read Line:",str(line))

# Get the current position of the file.
pos = fo.tell()
print("Current Position:",str(pos))


fow.write("teste1\n")
fow.write("teste1\n")
fow.write("teste1\n")
fow.write("teste1\n")

pos = fow.tell()

print("Current Position:",str(pos))

# Close opend file
fo.close()