#!/usr/bin/env python
# coding: utf8

from requests import get
import message
import json

class Telegram:

	def __init__(self, botToken, channelId):
		self.botToken = botToken
		self.channelId = channelId
		self.sendStickerURL = "https://api.telegram.org/bot"+self.botToken+"/sendSticker"
		self.sendMessageURL = "https://api.telegram.org/bot"+self.botToken+"/sendMessage"
		self.sendLocationURL = "https://api.telegram.org/bot"+self.botToken+"/sendLocation"
		with open('telegramStickers.json') as f:
			self.stickers = json.load(f)

	def sendMessage(self, message):
		sendMessagePayload = {'text': message ,
								'chat_id': self.channelId,
								'parse_mode' : 'html'}
		r = get(self.sendMessageURL, params = sendMessagePayload)
		return r

	def sendSticker(self, sticker):
		sendStickerPayload = {'chat_id' : self.channelId,
								'sticker' : sticker}
		r = get(self.sendStickerURL, params = sendStickerPayload)
		return r

	def sendLocation(self, lat, lon):
		sendLocationPayload = {'chat_id' : self.channelId,
								'longitude' : lon,
								'latitude' : lat}
		r = get(self.sendLocationURL, params = sendLocationPayload)
		return r

	def sendPokemonNotification(self, pokemon):
		# get Sticker
		if(str(pokemon.pokemonId) in self.stickers['sticker_pkl']):
			self.sendSticker(self.stickers['sticker_pkl'][str(pokemon.pokemonId)])
		msg = message.getMessage(pokemon)
		self.sendMessage(msg)
		self.sendLocation(pokemon.lat, pokemon.lon)