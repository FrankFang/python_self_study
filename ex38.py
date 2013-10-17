ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(' ')
more_stuff = "Day,Night,Sone,Frisbee,Corn,Banana,Girl,Boy".split(',')

while len(stuff) != 10:
    next_one = more_stuff.pop()
    stuff.append(next_one)

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

