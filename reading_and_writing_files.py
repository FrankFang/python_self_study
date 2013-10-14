__metaclass__ = type

from sys import argv

script , filename = argv
print("We're going to erase %r."%filename)
print("If you don't want that, hit Ctrl-C.")
print("If you do want that, hit RETURN.")

raw_input('?')

print("Opening the file")
target = open(filename,'w')
print("Thuncating the file. Bye.")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1  = raw_input("line 1:")
line2  = raw_input("line 2:")
line3  = raw_input("line 3:")

print("I'm going to write there to the file.")

target.write(line1)
target.write(line2)
target.write(line3)

print("Finally, close it.")
target.close()


