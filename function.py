__metaclass__ = type

def print_two(*args):
    arg1, arg2 = args
    print("%r %r" % (arg1, arg2))

def print_two_too(arg1, arg2):
    print("%r %r" % (arg1, arg2))

print_two(1,2)
print_two_too(1,2)
