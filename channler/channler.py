from threading import Thread
import time
import logging

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
		self.pokemonDbWrapper = monDb.PokemonDb()

		logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.INFO)
		self.logger = logging.getLogger(__name__)
		

		if(self.messenger == 'telegram'):
			self.notificationCnx = telegram.Telegram(self.botToken, self.channelId)
		else:
			raise ValueError('Unknown messenger type ' + self.messenger + " on "+self.channelName+". Please check channels.json")

	def run(self):
		self.logger.info("Thread " + self.threadName + " is initialized and ready to use")
		self.logger.info("Channel " + self.channelName + " is up")

	def check(self):

		if(self.type == 'pokemon'):
			data = self.pokemonDbWrapper.getPokemon()
			self.logger.info("%s found %s new Pokemon", self.channelName, str(len(data)))

			for pokemon in data:
				if(not utils.checkIfSpawnIsExpired(pokemon.disappear_timestamp)):
					if(not self.sentManager.checkIfAlreadySent(pokemon.encounterId)):
						if(utils.isInGeofence(self.includeArea, pokemon.lat, pokemon.lon) and utils.isNotInGeofence(self.excludeArea, pokemon.lat, pokemon.lon)):
							if(self.filter.isFilterSatisfied(pokemon)):
								self.logger.info("Pokemon with encounter %s id will be sent to: %s",pokemon.encounterId, self.channelName)
								self.notificationCnx.sendPokemonNotification(pokemon)
								self.sentManager.addEncounterToAlreadySent(pokemon.encounterId, pokemon.disappear_timestamp)
