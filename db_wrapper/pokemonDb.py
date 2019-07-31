import connector
from utils import utils as u
from utils import configParser as cp
from model import pokemon as pkm
import datetime
import time
class PokemonDb:

	def __init__(self):
		# get database schema
		config = cp.readConfig()
		self.schema = config.get('database', 'db_schema')
		self.lastDatabseRequestTime = time.time()

	def getPokemon(self):
		if(self.schema == 'rm'):
			return self.getPokemonFromRocketmapDatabase()
		elif (self.schema == 'rdm'):
			return self.getPokemonFromRdmDatabase()
		else:
			raise ValueError('Unknown schema ' + self.schema + ".")

	def getPokemonFromRocketmapDatabase(self):
		try:
			databaseObj = connector.DatabaseConnector()
			cnx = databaseObj.connect()

			cursor = cnx.cursor(dictionary=True)
			allVisiblePokemon = ("SELECT * FROM pokemon WHERE disappear_time > CONVERT_TZ(NOW(), @@session.time_zone, '+00:00');")
			cursor.execute(allVisiblePokemon)
			result_set = cursor.fetchall()

			cursor.close()
			cnx.close()

			self.lastDatabseRequestTime = time.time()

			pokemons = []
			for pokemonRelation in result_set:
				pokemons.append(self._parseRMRelationToMode(pokemonRelation))

		except Exception as e:
				print (e)
				pokemon = []
		
		return pokemons

	def _parseRMRelationToMode(self, pokemonRelation):

		pokemon = pkm.Pokemon()

		pokemon.encounterId = pokemonRelation['encounter_id']
		pokemon.pokemonId = pokemonRelation['pokemon_id']
		pokemon.lat = pokemonRelation['latitude']
		pokemon.lon = pokemonRelation['longitude']
		pokemon.atkIv = pokemonRelation['individual_attack']
		pokemon.defIv = pokemonRelation['individual_defense']
		pokemon.staIv = pokemonRelation['individual_stamina']
		pokemon.iv = u.calcIV(pokemon.atkIv, pokemon.defIv, pokemon.staIv)
		pokemon.form = u.getForm(pokemon.pokemonId , pokemonRelation['form'])
		pokemon.gender = u.getGender(pokemonRelation['gender'])
		pokemon.weather = u.getWeather(pokemonRelation['weather_boosted_condition'])
		pokemon.level = u.getPokemonLevel(pokemonRelation['cp_multiplier'])
		pokemon.cp = pokemonRelation['cp']
		pokemon.disappear_timestamp = pokemonRelation['disappear_time']
		pokemon.disappear_time = u.getDisapearTime(pokemonRelation['disappear_time'])
		pokemon.duration = u.getPokemonDurationTime(pokemonRelation['disappear_time'])

		return pokemon

	def getPokemonFromRdmDatabase(self):
		try:
		
			databaseObj = connector.DatabaseConnector()
			cnx = databaseObj.connect()

			cursor = cnx.cursor(dictionary=True)
			allVisiblePokemon = ("SELECT from_unixtime(expire_timestamp) AS disappear_time, id, pokemon_id, form, atk_iv, def_iv, sta_iv, gender, cp, weather, lat, lon, iv, level FROM pokemon WHERE updated >" + str(self.lastDatabseRequestTime) +";")
			cursor.execute(allVisiblePokemon)
			result_set = cursor.fetchall()

			cursor.close()
			cnx.close()

			self.lastDatabseRequestTime = time.time()
			
			pokemons = []
			for pokemonRelation in result_set:
				pokemons.append(self._parseRDMRalationToModel(pokemonRelation))
			
		except Exception as e:
			print (e)
			pokemons = []
		
		return pokemons

	def _parseRDMRalationToModel(self, pokemonRelation):

		pokemon = pkm.Pokemon()

		pokemon.encounterId = pokemonRelation['id']
		pokemon.pokemonId = pokemonRelation['pokemon_id']
		pokemon.lat = pokemonRelation['lat']
		pokemon.lon = pokemonRelation['lon']
		pokemon.iv = pokemonRelation['iv']
		pokemon.atkIv = pokemonRelation['atk_iv']
		pokemon.defIv = pokemonRelation['def_iv']
		pokemon.staIv = pokemonRelation['sta_iv']
		pokemon.form = u.getForm(pokemon.pokemonId , pokemonRelation['form'])
		pokemon.gender = u.getGender(pokemonRelation['gender'])
		pokemon.weather = u.getWeather(pokemonRelation['weather'])
		pokemon.level = pokemonRelation['level']
		pokemon.cp = pokemonRelation['cp']
		pokemon.disappear_timestamp = pokemonRelation['disappear_time']
		pokemon.disappear_time = u.getDisapearTime(pokemonRelation['disappear_time'])
		pokemon.duration = u.getPokemonDurationTime(pokemonRelation['disappear_time'])

		return pokemon

