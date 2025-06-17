import os

os.system('uncompress firefox.log.gz')
fo = open("firefox.log", "rw+")
line = fo.readline()
while(line):
	if (line != "https://en.wikipedia.org/wiki/The_Conversation\n"):
		print(line)
	line = fo.readline()
