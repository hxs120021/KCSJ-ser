from queue import Queue
from NetSocket.RecvMsg import RecvMsg
from NetSocket.SendCheck import SendCheck
from NetSocket.SendMsg import SendMsg
from NetSocket.WaitSearch import WaitSearch
from NetSocket.WaitEqu import WaitEqu
from Calc.Calc import Calc

checkDatas = Queue()
calcDatas = Queue()
online = ["ICU996^equ996^testname^man^40"]
sendip = "192.168.1.102"
#sendalrm = SendMsg("127.0.0.1", "error!")
#sendalrm.send()

waitEqu = WaitEqu(online)
waitEqu.waitEqu()

recvmsg = RecvMsg(checkDatas, calcDatas)
recvmsg.Recv()

waitwin = WaitSearch(online)
waitwin.wasend()

#oo = input()
sendcheck = SendCheck(checkDatas, sendip)
sendcheck.whilesend()

calc = Calc(calcDatas)
calc.calc()

#test
#while(True):
#	data = input()
#	calcDatas.put(data)
#test

