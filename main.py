import Counter as w
from klienci.KlientZwykly import *
from klienci.KlientVIP import *
from myQueue import myQueue
import time
from signal import *
# #
import sys
from myGui import *

if sys.argv[1] != "start":
    os.kill(os.getppid(),9)
    print(os.getppid())

g = myGui()
while not g.exit:
    g.go()

if myGui.restart:
    os.system("python3 main.py nie plagiatowałem")

nananana




# tab1=["dzien","b","c"]
# tab2=["dobry","e","f"]
# # najpier iterator potem zawartość
# for i,x in zip(tab1,tab2):
#     print(i,x)
#
