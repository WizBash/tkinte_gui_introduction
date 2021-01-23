import logging
logfomart="%(levelname)s %(asctime)s --- %(message)ss"
logging.basicConfig(filename='logfile.log',level=logging.DEBUG,format=logfomart)
logger = logging.getLogger()

def add():
	a=7
	b=8
	c=a+b
	print(c)

	logger.info(add)


add()
