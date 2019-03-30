import connector
from utils import configParser as cp

class PokemonDb:

	def __init__(self):
		# get database schema
		config = cp.readConfig()
		self.schema = config.get('database', 'db_schema')
		print("Using schema", self.schema)

	def getPokemon(self):
		if(self.schema == 'rm'):
			return self.getPokemonFromRocketmapDatabase()
		elif (self.schema == 'rdm'):
			return self.getPokemonFromRdmDatabase()
		else:
			raise ValueError('Unknown schema ' + self.schema + ".")

	def getPokemonFromRocketmapDatabase(self):
		databaseObj = connector.DatabaseConnector()
		cnx = databaseObj.connect()

		cursor = cnx.cursor(dictionary=True)
		allVisiblePokemon = ("SELECT * FROM pokemon WHERE disappear_time > CONVERT_TZ(NOW(), @@session.time_zone, '+00:00');")
		cursor.execute(allVisiblePokemon)
		result_set = cursor.fetchall()

		cursor.close()
		cnx.close()

		return result_set


	def getPokemonFromRdmDatabase(self):
		databaseObj = connector.DatabaseConnector()
		cnx = databaseObj.connect()

		cursor = cnx.cursor(dictionary=True)
		allVisiblePokemon = ("SELECT from_unixtime(expire_timestamp) AS disappear_time, id AS encounter_id, pokemon_id AS pokemon_id, form AS form, atk_iv AS individual_attack,def_iv AS individual_defense,sta_IV AS individual_stamina,gender AS gender,cp AS cp,weather AS weather_boosted_condition, lat AS latitude, lon AS longitude FROM pokemon WHERE from_unixtime(expire_timestamp) > CONVERT_TZ(NOW(), @@session.time_zone, '+00:00');")
		cursor.execute(allVisiblePokemon)
		result_set = cursor.fetchall()

		cursor.close()
		cnx.close()

		return result_set

