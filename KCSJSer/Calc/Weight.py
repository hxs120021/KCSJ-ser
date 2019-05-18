import sys
from Data.DataType import DataType

class Weight(object):
	data = 0
	hrDatas = []
	spo2Datas = []
	tempDatas = []
	def __init__(self):
		#self.data = data
		#self.dataType = dataType
		self.clear()
		pass

	def clear(self):
		self.hrDatas.clear()
		self.spo2Datas.clear()
		self.tempDatas.clear()
		for i in range(0, 20):
			self.hrDatas.append(75)
			self.spo2Datas.append(99)
			self.tempDatas.append(36.5)

	def calc(self, data, dataType):
		datas = []
		if(dataType == DataType.hr):
			datas = self.hrDatas
		elif(dataType == DataType.spo2):
			datas = self.spo2Datas
		else:
			datas = self.tempDatas
		if(len(datas) > 20):
			datas.pop(0)
		we = [3/35, 2/35, 3/70, 1/70]
		avg = 0
		for v in range(0,len(datas)):
			avg += (datas[v] * we[int(v/5)])
		cha = abs(avg - data)
		if(cha > self.isInRange(dataType)):
			self.clear()
			return False
		datas.append(data)
		return True

	def isInRange(self, dataType):
		if(dataType == DataType.hr):
			return 12
		elif(dataType == DataType.spo2):
			return 0.9
		elif(dataType == DataType.temp):
			return 0.6