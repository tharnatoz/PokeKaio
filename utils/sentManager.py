#!/usr/bin/env python
# coding: utf8

import datetime as dt

class SentManager:

	def __init__(self):
		self.already_sent = []


	def checkIfAlreadySent(self, encounter_id):
		for encounter in self.already_sent:
			if str(encounter_id) == str(encounter["encounter_id"]):
				return True
		return False

	def addEncounterToAlreadySent(self, encounter_id, disappear_time):
		print("Add enc to already sent")
		enc = self.getAlreadySentObj(encounter_id, disappear_time)
		self.already_sent.append(enc)


	def getAlreadySentObj(self, encounter_id, disappear_time):
		disappear_time = disappear_time + dt.timedelta(hours=1)
		return {"encounter_id" : encounter_id , "disappear_time" : disappear_time}

	def cleanEncounters(self):
		for encounter in self.already_sent:
			if encounter["disappear_time"] < dt.datetime.now() - dt.timedelta(minutes=70):
				self.already_sent.remove(encounter)

