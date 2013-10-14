__metaclass__ = type

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

dict = { 'age': age, 'height': height, 'weight': weight }
print( "So, you are %(age)r old, %(height)r tall and %(weight)r heavy" % dict)

