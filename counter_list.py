__metaclass__= type
class CounterList(list):
	def __init__(self, *args):
		super(CounterList,self).__init__(*args)
		self.counter = 0
	def __getitem__(self, index):
		self.counter += 1
		print(self.counter)
		return super(CounterList,self).__getitem__(index)

c1 = CounterList(range(10))
c1.reverse()
del c1[3:6]
c1[4]+c1[2]