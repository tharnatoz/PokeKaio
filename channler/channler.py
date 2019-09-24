import time
import threading
import logging

from filters import filterManager as fm
from db_wrapper import dbManager as dbm

from utils import utils
from notification import telegram
from utils import sentManager as sm

class Channler(threading.Thread):


	def __init__(self, channelConfig, options, reverseGeocoder):
		threading.Thread.__init__(self)

		self.channelName = channelConfig['name']
		self.messenger = channelConfig['messenger']
		self.type = channelConfig['type']
		self.channelId = channelConfig['channelId']
		self.botToken = channelConfig['botToken']
		self.includeArea = utils.parseGeofence(channelConfig['geofence'])
		self.excludeArea = utils.parseGeofence(channelConfig['geofence_exclude'])
		self.sentManager = sm.SentManager()
		self.checkInterval = options['checkInterval']

		self.rgc = reverseGeocoder
		
		# database manager
		self.databaseManager = dbm.DbManager(options['database'])
		self.db = self.databaseManager.getDbBridge()


		# filter manager
		self.filterManager = fm.FilterManager(channelConfig['filter'])
		self.filter = self.filterManager.getFilter()

		logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.INFO)
		self.logger = logging.getLogger(__name__)
		

		if(self.messenger == 'telegram'):
			self.notificationCnx = telegram.Telegram(self.botToken, self.channelId, self.channelName)
		else:
			raise ValueError('Unknown messenger type ' + self.messenger + " on "+self.channelName+". Please check channels.json")

	def run(self):
		self.logger.info("Thread is initialized and ready to use")
		self.logger.info("Channel %s is up", self.channelName)

		while True:
			self.check()
			self.logger.info("%s is now waiting for %d seconds", self.channelName, self.checkInterval )
			time.sleep(self.checkInterval)


	def check(self):
		if(self.type == 'pokemon'):
			
			data = self.db.getPokemonData()
			self.logger.info("%s found %s new Pokemon", self.channelName, str(len(data)))

			for pokemon in data:
				if(not utils.checkIfSpawnIsExpired(pokemon.disappear_timestamp)):
					if(not self.sentManager.checkIfAlreadySent(pokemon.encounterId)):
						if(utils.isInGeofence(self.includeArea, pokemon.lat, pokemon.lon) and utils.isNotInGeofence(self.excludeArea, pokemon.lat, pokemon.lon)):
							if(self.filter.isSatisfied(pokemon)):
								address = ""
								if self.rgc is not None:
									address = self.rgc.getAddress(pokemon.lat, pokemon.lon)
								self.logger.info("Pokemon with encounter %s id will be sent to: %s",pokemon.encounterId, self.channelName)
								self.notificationCnx.sendPokemonNotification(pokemon, address)
								self.sentManager.addEncounterToAlreadySent(pokemon.encounterId, pokemon.disappear_timestamp)
