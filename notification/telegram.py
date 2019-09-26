#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from . import message
import json
import logging

class Telegram:

	def __init__(self, botToken, channelId, channelName):

		logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.ERROR)
		self.logger = logging.getLogger(__name__)

		self.botToken = botToken
		self.channelId = channelId
		self.channelName = channelName
		self.sendStickerURL = "https://api.telegram.org/bot"+self.botToken+"/sendSticker"
		self.sendMessageURL = "https://api.telegram.org/bot"+self.botToken+"/sendMessage"
		self.sendLocationURL = "https://api.telegram.org/bot"+self.botToken+"/sendLocation"
		with open('telegramStickers.json') as f:
			self.stickers = json.load(f)

	def sendMessage(self, message):
		sendMessagePayload = {'text': message ,
								'chat_id': self.channelId,
								'disable_web_page_preview': True,
								'parse_mode' : 'html'}
		r = get(self.sendMessageURL, params = sendMessagePayload)

		self.checkForErrors(r)

		return r

	def sendSticker(self, sticker):
		sendStickerPayload = {'chat_id' : self.channelId,
								'sticker' : sticker}
		r = get(self.sendStickerURL, params = sendStickerPayload)
		
		self.checkForErrors(r)

		return r

	def sendLocation(self, lat, lon):
		sendLocationPayload = {'chat_id' : self.channelId,
								'longitude' : lon,
								'latitude' : lat}
		r = get(self.sendLocationURL, params = sendLocationPayload)

		self.checkForErrors(r)

		return r

	def sendPokemonNotification(self, pokemon, address=""):
		# get Sticker
		if(str(pokemon.pokemonId) in self.stickers['sticker_pkl']):
			self.sendSticker(self.stickers['sticker_pkl'][str(pokemon.pokemonId)])
		msg = message.getMessage(pokemon, address)
		self.sendMessage(msg)
		self.sendLocation(pokemon.lat, pokemon.lon)

	def checkForErrors(self, response):
		resp  = json.loads(response.text)
		if(resp['ok'] == False):
			self.logger.error("Message could not be sent to channle %s: %s",  self.channelName, resp['description'])



		