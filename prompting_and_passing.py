__metaclass__ = type

from sys import argv
script, user = argv

prompt = '> '

print ("Hi %(user)s, I'm the $(script)s script." % { 'script': script, 'user' : user})
print("I'd like to ask you a few questions.")
print("Do you like me, %(user)s" % {'user': user})
like = raw_input(prompt)
print ("Where do you live, %(user)s" % {'user': user})
live = raw_input(prompt)

print("""
Alright, so you said you %(like)r me.
You live in %(live)r.
""" % {'like': like, 'live': live})
