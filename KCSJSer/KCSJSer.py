from queue import Queue
from NetSocket.RecvMsg import RecvMsg
from NetSocket.SendCheck import SendCheck
from NetSocket.SendMsg import SendMsg
from NetSocket.WaitSearch import WaitSearch
from NetSocket.WaitEqu import WaitEqu
from Calc.Calc import Calc

checkDatas = Queue()
calcDatas = Queue()
#online = ["ICU996^equ996^张三^man^40"]
online = []
#发送地址
sendip = "192.168.43.246"
#本地监听地址
bindip = "192.168.43.175"
#sendalrm = SendMsg("127.0.0.1", "error!")
#sendalrm.send()

waitEqu = WaitEqu(online, bindip)
waitEqu.waitEqu()

recvmsg = RecvMsg(checkDatas, calcDatas, bindip)
recvmsg.Recv()

waitwin = WaitSearch(online, bindip)
waitwin.wasend()

#oo = input()
sendcheck = SendCheck(checkDatas, bindip)
sendcheck.whilesend()

calc = Calc(calcDatas)
calc.calc()

#test
#while(True):
#	data = input()
#	calcDatas.put(data)
#test

