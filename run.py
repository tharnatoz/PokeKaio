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
	i = 0
	for channel in channelsConfig['pokemon']:
		if (channel['isActive'] == "true"):
			tmpChannler = channler.Channler(channel, str(i))
			channelList.append(tmpChannler)
			i += 1

	for channel in channelList:
			channel.start()

	while(True):
		for channel in channelList:
			channel.check()
		time.sleep(checkInterval)


