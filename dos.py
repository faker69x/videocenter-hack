from threading import Thread
import api

thrds = []

def addEntries():
	for letters in ["fuck", "magic", "http", "api"]:
		t = Thread(target=api.addFrikas, args=(letters,))
		thrds.append(t)
		t.start()
	for t in thrds:
		t.join()


def spam():
	for y in range(1, 10):
		for i in range(1,1000):
			x = Thread(target=api.execx)
			#x = Thread(target=api.httpDos)
			thrds.append(x)
			x.start()
		for x in thrds:
			x.join()

		print(error_count)
		print("1.000 Threads finished")

##addEntries()
spam()
