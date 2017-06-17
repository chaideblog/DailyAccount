import time

def getCurrentTime():
	return list(time.localtime(time.time()))

def getCurrentYear():
	return list(time.localtime(time.time()))[0]

def getCurrentMonth():
	return list(time.localtime(time.time()))[1]

def getCurrentDay():
	return list(time.localtime(time.time()))[2]