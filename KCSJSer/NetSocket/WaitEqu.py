from Task.BaseThread import BaseThread
import socket

class WaitEqu(object):
	def __init__(self, online):
		self.online = online
		pass

	def func(self):
		print("wait Equ 6698")
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(('0.0.0.0', 6698))
		server.listen(10)
		while(True):
			conn, addr = server.accept()
			try:
				data = conn.recv(1024)
				data = data.decode("utf-8")
				print(data)
				self.online.append(data)
			except ConnectionResetError as e:
				print(str(e))

			conn.close()

	def waitEqu(self):
		waitEqu = BaseThread(self.func)
		waitEqu.start()
