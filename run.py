#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import signal
import logging


from channler import channler
from utils import configParser as cp

version = '1.2.0'

if __name__ == "__main__":

	logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.INFO)
	logger = logging.getLogger(__name__)

	logger.info("#############################")
	logger.info("PokeKaio - v. %s",  version)
	logger.info("#############################")
	logger.info("Load config...")
	
	# loadconfig
	config = cp.readConfig()
	checkInterval = int(config.get('channler', 'checkInterval'))
	logger.info("Databse Checkinterval is set to %s", checkInterval)

	logger.info("Using Databaseshema: %s" , config.get('database', 'db_schema'))

	channelList = []

	with open('config/channels.json') as f:
		channelsConfig = json.load(f)

	# create pkm channel
	for channel in channelsConfig['pokemon']:
		if (channel['isActive'] == "true"):
			tmpChannler = channler.Channler(channel, checkInterval)
			channelList.append(tmpChannler)
			logger.info("Found channel config: %s", tmpChannler.channelName)

	logger.info("A total of %d channels will be initilized", len(channelList))

	if (len(channelList) == 0):
		logger.error('No Channels found. Please go to config/channels.json and configure at least one')
		exit()

	# Register the signal handlers
	#signal.signal(signal.SIGTERM, service_shutdown)
	
	#signal.signal(signal.SIGINT, service_shutdown)

	for channel in channelList:
		channel.setDaemon(True)
		channel.start()
	
		# run forever
	while(True):
		time.sleep(0.5)

 
	print('Exiting main program')	
