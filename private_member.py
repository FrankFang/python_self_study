__metaclass__ = type
class Person:
	__name = ''
	def setName(self, name):
		self.__name = name
	def getName(self):
		return self.__name
	def greet(self):
		print "Hello, I'm %s" % self.__name

foo = Person()
bar = Person()
foo.setName('Luke')
bar.setName('Capser')
foo.greet()
bar.greet()
# print(foo.__name)  # error!