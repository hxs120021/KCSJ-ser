class Equipment(object):
	def __init__(self, data):
		datas = data.split('^')
		self.bid = datas[0]
		self.sid = datas[1]
		self.name = datas[2]
		self.sex = datas[3]
		self.age = datas[4]

	def toString(self):
		result = self.bid+'^'+self.sid+'^'+self.name+'^'+self.sex+'^'+self.age
		return result