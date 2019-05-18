from Data.DataType import DataType

class Threshold(object):

	def __init__(self):
		#self.data = data
		#self.dataType = dataType
		pass

	def calc(self, data, dataType):
		if(dataType ==DataType.hr):
			if(data > 60 and data < 100):
				return True
			else:
				return False
		elif(dataType == DataType.spo2):
			if(data >= 96 and data < 100):
				return True
			else:
				return False
		elif(dataType == DataType.temp):
			if(data > 36 and data < 37):
				return True
			else:
				return False