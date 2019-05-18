import socket
from Task.BaseThread import BaseThread
from Data.Check import Check
from Data.Equipment import Equipment
#等待查询条件，查询到之后返回结果
#1.用什么存储当前在线设备
#2.没想出来
class WaitSearch(object):
	def __init__(self, online):
		#self.ip = ip
		self.online = online

	def wasend(self):
		task = BaseThread(self.func)
		task.start()

	def func(self):
		#equs = []
		print("wait win")
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(("127.0.0.1", 9967))
		server.listen(10)
		while(True):
			conn, addr = server.accept()
			try:
				searchInfo = conn.recv(1024)
				searchInfo = searchInfo.decode("utf-8")
				print(searchInfo)
				data = self.GetMsg(self.online, searchInfo)
				conn.send(data.encode())
				print("send:"+data)
			except ConnectionError as e:
				print(str(e))
				conn.close()
		server.close()


	def GetMsg(self, equs, info):
		result = ""
		for v in equs:
			if(info in v):
				result += v
				result += " "
		return result