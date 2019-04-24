import Window as w
from klienci.KlientZwykly import *
from MyQueue import MyQueue
import time

time.sleep(1)

zq = MyQueue()
zq.push(KlientZwykly('b'))
print(zq)
zq.push(KlientZwykly('c'))
zq.push(KlientZwykly('d'))
print(zq)
time.sleep(1)
zq.pop()
print(zq)
time.sleep(1)
zq.pop()
time.sleep(1)
zq.pop()