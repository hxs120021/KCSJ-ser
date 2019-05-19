from Data.DataType import DataType
from Task.BaseThread import BaseThread
from Calc.Threshold import Threshold
from Calc.Weight import Weight
from NetSocket.SendMsg import SendMsg
from Data.Check import Check

class Calc(object):
	
	def __init__(self, queue):
		self.queue = queue
		self.winip = "10.63.2.115"
		self.piip = "10.63.10.7"

	def calc(self):
		calctask = BaseThread(self.func)
		calctask.start()

	def func(self):
		weight = Weight()
		thresh = Threshold()
		i = 0
		while(True):
			print("start wait queue:")
			data = self.queue.get()
			check = Check(data)
			state1 = weight.calc(check.hr, DataType.hr)
			state2 = thresh.calc(check.hr, DataType.hr)
			state3 = weight.calc(check.spo2, DataType.spo2)
			state4 = thresh.calc(check.spo2, DataType.spo2)
			state5 = weight.calc(check.temp, DataType.temp)
			state6 = thresh.calc(check.temp, DataType.temp)
			if((not state1) or (not state2) or (not state3) or (not state4) or (not state5)):
				#print("warning!")
				#需要分别发给win和pi
				alrm = SendMsg(self.winip, "alrm")
				alrm = SendMsg(self.piip, "alrm")

		#if(self.weight.calc() and self.thresh.isInTreshold()):
		#	return
		#else:
		#	alrm = SendMsg("127.0.0.1", "alrm")
		#	alrm = SendMsg("127.0.0.2", "alrm")
