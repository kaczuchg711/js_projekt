import Window as w
from klienci.KlientZwykly import *
from klienci.KlientVIP import *
from myQueue import myQueue
import time
from myGui import *


g = myGui()

while not g.exit:
    g.events()
    g.go()

