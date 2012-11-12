class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
	def setSize(self, size):
		self.width, self.height = size
	def getSize(self):
		return self.width, self.height
	# here
	size = property(getSize, setSize)
	def n():
	    doc = "The n property."
	    def fget(self):
	        return self._n
	    def fset(self, value):
	        self._n = value
	    def fdel(self):
	        del self._n
	    return locals()
	n = property(**n())

r = Rectangle()
r.width = 10
r.height = 5
print(r.size)
print(r.getSize())
r.setSize((15,10))
print(r.width)