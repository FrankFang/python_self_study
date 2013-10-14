__metaclass__ = type
import sys
class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a + self.b
		return self.a
	def __iter__(self):
		return self

fibs = Fibs()
fibs = iter(fibs)
# print(fibs.next())
print('....')
for f in fibs:
    print (f)
    if f > 100:
		break
sys.exit()
