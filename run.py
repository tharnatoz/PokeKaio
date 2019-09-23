#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import signal
import logging


from channler import channler
from utils import configParser as cp
from reverseGeoCoder import reverseGeoCoder as rgcClass

version = '1.3'

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


	# check for reverse geo coding
	rgc = None
	reverseGeoCoding = bool(config.get('ReverseGeocoding', 'enable_reverse_geocoding'))
	if (reverseGeoCoding):
		googleMapsApiKey = config.get('ReverseGeocoding', 'google_maps_api_key')
		rgc = rgcClass.ReverseGeoCoder(googleMapsApiKey)
		if googleMapsApiKey == "":
			logger.error('Please add a google maps api key to use reverse geocoding or disable this feature')
			exit()

	

	# load channels
	channelList = []

	with open('config/channels.json') as f:
		channelsConfig = json.load(f)

	# create pkm channel
	for channel in channelsConfig['pokemon']:
		if (channel['isActive'] == "true"):
			tmpChannler = channler.Channler(channel, checkInterval, rgc)
			channelList.append(tmpChannler)
			logger.info("Found channel config: %s", tmpChannler.channelName)

	logger.info("A total of %d channels will be initilized", len(channelList))

	if (len(channelList) == 0):
		logger.error('No Channels found. Please go to config/channels.json and configure at least one')
		exit()

	for channel in channelList:
		channel.setDaemon(True)
		channel.start()
	
		# run forever
	while(True):
		time.sleep(0.5)

 
	print('Exiting main program')	
