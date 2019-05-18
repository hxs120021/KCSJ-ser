import socket
from Task.BaseThread import BaseThread

#发送报警
class SendMsg:
	def __init__(self, ip ,message):
		self.ip = ip
		self.message = message
		
	def send(self):
		task = BaseThread(self.func)
		task.start()

	def func(self):
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((self.ip, 9970))
		client.send(self.message.encode("utf-8"))
		msg = client.recv(1024)
		client.close()

	