#!/usr/bin/env python
# coding: utf8
import json
import time

from channler import channler
from utils import configParser as cp



if __name__ == "__main__":


	# loadconfig
	config = cp.readConfig()
	checkInterval = int(config.get('channler', 'checkInterval'))

	channelList = []

	with open('config/channels.json') as f:
		channelsConfig = json.load(f)

	# create pkm channel
	for channel in channelsConfig['pokemon']:
		tmpChannler = channler.Channler(channel)
		channelList.append(tmpChannler)

	while(True):
		for channel in channelList:
			channel.run()
		time.sleep(checkInterval)
