
class Check(object):
	def __init__(self, data):
		datas = data.split('^')
		self.hr = int(datas[0])
		self.spo2 = float(datas[1])
		self.temp = float(datas[2])

	def toString(self):
		result = str(self.hr)+'^'+str(self.spo2)+'^'+str(self.temp)
