from threading import Thread
import time


from utils import utils
from notification import telegram
from filters import filter
from db_wrapper import pokemonDb as monDb
from utils import sentManager as sm

class Channler(Thread):

	def __init__(self, channelConfig, name):
		Thread.__init__(self)

		self.threadName = name
		self.channelName = channelConfig['name']
		self.messenger = channelConfig['messenger']
		self.type = channelConfig['type']
		self.channelId = channelConfig['channelId']
		self.botToken = channelConfig['botToken']
		self.filter = filter.Filter(channelConfig['filter'])
		self.includeArea = utils.parseGeofence(channelConfig['geofence'])
		self.excludeArea = utils.parseGeofence(channelConfig['geofence_exclude'])
		self.sentManager = sm.SentManager()

		if(self.messenger == 'telegram'):
			self.notificationCnx = telegram.Telegram(self.botToken, self.channelId)
		else:
			raise ValueError('Unknown messenger type ' + self.messenger + " on "+self.channelName+". Please check channels.json")

	def run(self):
		print "Thread " + self.threadName + " is initialized and ready to use"
		print "Channel " + self.channelName + " is up"

	def check(self):
		# first get data
		# print "Thread: " + self.threadName + " is checking data"
		if(self.type == 'pokemon'):
			data = monDb.getPokemon()
			for pokemon in data:
				if(not utils.checkIfSpawnIsExpired(pokemon['disappear_time'])):
					if(not self.sentManager.checkIfAlreadySent(pokemon['encounter_id'])):
						if(utils.isInGeofence(self.includeArea, pokemon) and utils.isNotInGeofence(self.excludeArea, pokemon)):
							if(self.filter.isFilterSatisfied(pokemon)):
								self.notificationCnx.sendPokemonNotification(pokemon)
								self.sentManager.addEncounterToAlreadySent(pokemon['encounter_id'], pokemon['disappear_time'])
					else:
						print "Found Pokemon but not sending cause is already sent"
				else:
					print "Pokemon is expired"
