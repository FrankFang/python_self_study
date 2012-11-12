__metaclass__ = type
class Person:
	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
	def greet(self):
		print "Hello, I'm %s" % self.name

foo = Person()
bar = Person()
foo.setName('Luke')
bar.setName('Capser')
foo.greet()
bar.greet()
print(foo.name)