import socket
from Task.BaseThread import BaseThread
from queue import Queue
#发送检测的数据
class SendCheck(object):

	def __init__(self,queue, ip):
		self.queue = queue
		self.ip = ip

	def whilesend(self):
		sendThread = BaseThread(self.func)
		sendThread.start()

	def func(self):
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		checkdata = self.queue.get()
		client.connect((self.ip, 9966))
		print("connect #####")
		while(True):
			try:
				client.send(checkdata.encode("utf-8"))
				data = client.recv(1024)
				print(data.decode("utf-8"))
				checkdata = self.queue.get()
			except ConnectionError as e:
				print(str(e))
				break
		client.close()