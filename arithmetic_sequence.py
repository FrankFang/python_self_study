#-*- coding: utf-8 -*-
def checkIndex(key):
	"""
	检查索引是否合法

	非负整数
	"""
	if not isinstance(key,(int,long)):raise TypeError
	if key < 0: raise IndexError

class ArithmeticSequence:
	def __init__(self, start=0, step=1):
		"""
		初始化算数序列

		start -- 序列钟的第一个值
		step -- 两个相邻值之间的差值
		changed -- 用户修改过的值的字典
		"""	
		self.start = start
		self.step = step
		self.changed = {}

	def __getitem__(self,key):
		checkIndex(key)
		try: 
			return self.changed[key]
		except KeyError:
			return self.start + key*self.step

	def __setitem__(self,key,value):
		checkIndex(key)
		self.changed[key] = value

s = ArithmeticSequence(1,2)
print(s[5])
print(s['fool'])
