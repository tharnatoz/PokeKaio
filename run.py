#!/usr/bin/env python
# coding: utf8
import json
import time
import logging


from channler import channler
from utils import configParser as cp

version = '1.1.5'

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
	i = 1
	for channel in channelsConfig['pokemon']:
		if (channel['isActive'] == "true"):
			tmpChannler = channler.Channler(channel, str(i))
			channelList.append(tmpChannler)
			logger.info("Found channel config: %s", tmpChannler.channelName)

			i += 1
	logger.info("A total of %d channels will be initilized", len(channelList))

	if (len(channelList) == 0):
		logger.error('No Channels found. Please go to config/channels.json and configure at least one')
		exit()

	for channel in channelList:
			channel.start()
	while(True):
		try:
		
			for channel in channelList:
				channel.check()
				logger.info("%s is now waiting for %d seconds", channel.channelName, checkInterval)
			time.sleep(checkInterval)
		except Exception as e:
			logger.error("An wild Exception appeared: %s", e) 

