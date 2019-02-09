from ConfigParser import SafeConfigParser



def readConfig():
	parser = SafeConfigParser()
	parser.read('config/config.ini')

	return parser
