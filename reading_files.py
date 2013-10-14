__metaclass__ = type

from sys import argv

script , filename = argv

markdown = open(filename)

print("Here's you file %(file)r:" %{'file':  filename})

print(markdown.read())

markdown.close()

print("Type the filename again:")

file_again = raw_input("> ")

markdown_again = open(file_again)

print( markdown_again.read())

markdown_again.close()
