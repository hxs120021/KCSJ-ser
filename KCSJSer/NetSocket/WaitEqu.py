from Task.BaseThread import BaseThread
import socket

class WaitEqu(object):
	def __init__(self, online, ip):
		self.online = online
		self.ip = ip
		pass

	def func(self):
		print("wait Equ 6698")
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((self.ip, 6698))
		server.listen(10)
		while(True):
			conn, addr = server.accept()
			try:
				print("connect equ is ok")
				data = conn.recv(1024)
				data = data.decode("utf-8")
				print(data)
				conn.send("".encode())
				self.online.append(data)
			except ConnectionResetError as e:
				print(str(e))

			conn.close()
		print("wati Equ end")

	def waitEqu(self):
		waitEqu = BaseThread(self.func)
		waitEqu.start()
