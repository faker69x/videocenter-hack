from threading import Thread
from subprocess import call
from random import randint
import time

SQL_QUERY = "sql_abfrage=SELECT+*+FROM+kunden%2C+videos%2C+ausleihe+WHERE+ausleihe.kunr+LIKE+%27%25{}%25%27+GROUP+BY+kunden.kustras++ORDER+BY+kunden.kuort&domain=Geschaeftsfuehrung&num=0&limit=10000&submit=Query+abschicken%21"

def execx():
    call(["./vcenter.sh", SQL_QUERY.format(randint(0, 2000))])

t = []

for y in range(1, 10):
	for i in range(1,1000):
		x = Thread(target=execx)
		t.append(x)
		x.start()
	for x in t:
		x.join()

	print("1.000 Threads finished")


