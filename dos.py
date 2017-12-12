from threading import Thread
import api

thrds = []

def addEntries():
	print "Editing database ..."
	statT = Thread(target=api.printStats)
	statT.start()

	for letters in ["fuck", "magic", "http", "api"]:
		t = Thread(target=api.addFrikas, args=(letters,))
		thrds.append(t)
		t.start()
	for i in range(0, 5):
		i = float(i)
		t = Thread(target=api.editUsers, args=(int(i/5 * 10000), int((i+1)/5 * 10000 - 1)))
		t.start()
	for i in range(0, 4):
		t = Thread(target=api.videoSpam, args=(i * 200, i * 200 + 200))
		thrds.append(t)
		t.start()
	for i in range(0, 5):
		i = float(i)
		t = Thread(target=api.editVideos, args=(int(i/5 * 9000), int((i+1)/5 * 9000 - 1)))
		t.start()
	for t in thrds:
		t.join()
	
	statT.do_run = False
	statT.join()
	print "Finished! They'll have fun!"


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


addEntries()
#spam()

exit(0)

