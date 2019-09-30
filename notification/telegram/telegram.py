#!/usr/bin/env python
# -*- coding: utf-8 -*-

from notification.baseMessenger import BaseMessenger
import time
import json


class Telegram(BaseMessenger):

	def __init__(self, channelName, config, locale=None):
		
		# config
		self.channelName = channelName
		self.botToken = config['botToken']
		self.channelId = config['channelId']
		
		# Telegram API endpoints
		self.sendStickerURL = "https://api.telegram.org/bot"+self.botToken+"/sendSticker"
		self.sendMessageURL = "https://api.telegram.org/bot"+self.botToken+"/sendMessage"
		self.sendLocationURL = "https://api.telegram.org/bot"+self.botToken+"/sendLocation"
		
		# google maps base url
		self.googleMapsUrl = "https://maps.google.com/?"

		# load stickers
		with open('notification/telegram/telegramStickers_mon.json') as f:
			self.stickers_mon = json.load(f)
		
		super(Telegram, self).__init__(config, locale)


	def sendPokemonNotification(self, pokemon, address=""):
		# get Sticker
		if(str(pokemon.pokemonId) in self.stickers_mon['sticker_pkl']):
			self._sendSticker(self.stickers_mon['sticker_pkl'][str(pokemon.pokemonId)])
		
		# get message from message.json
		if(pokemon.atkIv is not None):
			msg = self.message.getMessage('pokemon_info_detail')
		else:
			msg = self.message.getMessage('pokemon_info')
		
		# format message
		formattedMessage = self.message.replace(msg, pokemon.__dict__)
		
		# get spawntime valid/not valid message and append it on the message
		if(pokemon.expireTimestampVerified):
			formattedMessage = formattedMessage + self.message.getMessage('spawntime_valid')
		else:
			formattedMessage = formattedMessage + self.message.getMessage('spawntime_not_valid')
		
		# build the google maps address link 
		if(address is not ""):
			formattedMessage = formattedMessage + self._buildGoogleMapsAddressLink(address, pokemon.lat, pokemon.lon)
		
		# finally send message
		self._sendMessage(formattedMessage)
		
		# and send location
		self._sendLocation(pokemon.lat, pokemon.lon)

	
	def sendRaidNotification(self):
		pass

	def sendQuestNotification(self):
		pass 
	'''
	=====================================
	| Message Builder helper functions
	=====================================
	|
	| Helper function to build the telegram messages 
	| 
	|
	'''
	def _buildGoogleMapsAddressLink(self, address, lat, lon):
		address = address.encode("UTF-8")
		link = self._buildGoogleMapsLink(lat, lon)
		return"\n\n<a href='{link}'>{address}</a>".format(link=link, address=address)

	def _buildGoogleMapsLink(self, lat, lon):
		params = "daddr={lat},{lon}".format(
            lat=lat,
            lon=lon
        )
		return "{url_base}{params}".format(url_base=self.googleMapsUrl, params=params)

	
	'''
	=====================================
	| Telegram Api Functions
	=====================================
	|
	| All Api Calls 
	| 
	|
	'''

	# telegram api call for sending messages
	def _sendMessage(self, message):
		sendMessagePayload = {'text': message ,
								'chat_id': self.channelId,
								'disable_web_page_preview': True,
								'parse_mode' : 'html'}
		r = self.getRequest(self.sendMessageURL, params = sendMessagePayload)

		self.checkForErrors(r)

		return r

	# telegram api call for sending stickers
	def _sendSticker(self, sticker):
		sendStickerPayload = {'chat_id' : self.channelId,
								'sticker' : sticker}
		r = self.getRequest(self.sendStickerURL, params = sendStickerPayload)
		
		self.checkForErrors(r)

		return r
	# telegram api call for sending location 
	def _sendLocation(self, lat, lon):
		sendLocationPayload = {'chat_id' : self.channelId,
								'longitude' : lon,
								'latitude' : lat}
		r = self.getRequest(self.sendLocationURL, params = sendLocationPayload)

		self.checkForErrors(r)

		return r

    

	'''
	=====================================
	| Error checker
	=====================================
	|
	| Function that checks if some request are bad 
	| 
	|
	'''
	def checkForErrors(self, response):
		resp  = json.loads(response.text)
		if(resp['ok'] == False):
			self.logger.error("Message could not be sent to channel %s: %s",  self.channelName, resp['description'])