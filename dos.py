from threading import Thread
from subprocess import call
import time

def execx():
    call("./vcenter.sh")

t = []

for i in range(1,10000):
    x = Thread(target=execx)
    t.append(x)
     x.start()
for x in t:
    x.join()

    print("10.000 Threads finished")


