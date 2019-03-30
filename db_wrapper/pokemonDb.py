import connector
from utils import utils
from utils import configParser as cp
from model import pokemon as pkm

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
		allVisiblePokemon = ("SELECT from_unixtime(expire_timestamp) AS disappear_time, id, pokemon_id, form, atk_iv, def_iv, sta_iv, gender, cp, weather, lat, lon, iv, level FROM pokemon WHERE from_unixtime(expire_timestamp) > CONVERT_TZ(NOW(), @@session.time_zone, '+00:00');")
		cursor.execute(allVisiblePokemon)
		result_set = cursor.fetchall()

		cursor.close()
		cnx.close()

		pokemons = []
		for pokemonRelation in result_set:
			pokemons.append(self._parseRDMRalationToModel(pokemonRelation))

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
		pokemon.form = pokemonRelation['form']
		pokemon.gender = pokemonRelation['gender']
		pokemon.weather = pokemonRelation['weather']
		pokemon.level = pokemonRelation['level']
		pokemon.cp = pokemonRelation['cp']
		pokemon.disappear_time = pokemonRelation['disappear_time']


		return pokemon

