import Window as w
from klienci.KlientZwykly import *
from klienci.KlientVIP import *
from MyQueue import MyQueue
import time
from myGui import *


g = myGui()

while not g.exit:
    g.events()
    g.go()
