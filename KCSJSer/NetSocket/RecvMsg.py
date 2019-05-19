import socket
from Task.BaseThread import BaseThread

#接受检测数据
class RecvMsg:
	
	def __init__(self, checkQueue, calcQueue):
		self.checkQueue = checkQueue
		self.calcQueue = calcQueue

	def Recv(self):
		task = BaseThread(self.func)
		task.start()

	def func(self):
		print("wait check data")
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(('0.0.0.0', 9966))
		server.listen(10)
		while(True):
			conn, addr = server.accept()
			while(True):
				try:
					data = conn.recv(1024)
					data = data.decode('utf-8')
					print(data)
					self.checkQueue.put(data)
					self.calcQueue.put(data)
					#conn.send()
				except  ConnectionError as e:
					print("connect maby close" + str(e))
					break
			conn.close()
		server.close()
