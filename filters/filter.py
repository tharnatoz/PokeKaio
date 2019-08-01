from utils.utils import getFullStats

class Filter:

	def __init__(self, filterOptions):
		self.availableFilterTypes = ["whitelist", 'iv', 'whitelist_iv']

		if filterOptions['type'] not in self.availableFilterTypes:
			raise ValueError('Unknown filter type ' + filterOptions['type'] + '. Please check channels.json')

		self.filterConfig = filterOptions

	def isFilterSatisfied(self, pokemon):

		if (self.filterConfig['type'] == "whitelist"):
			return self.filterWhitelist(pokemon.pokemonId)
		elif (self.filterConfig['type'] == "iv"):
			return self.filterIv(pokemon)
		elif (self.filterConfig['type'] == "whitelist_iv"):
			return self.filterWhiteListIv(pokemon)
		else:
			return false

	def filterWhitelist(self, pokemonId):
		return pokemonId in self.filterConfig['whitelist'] and pokemonId not in self.filterConfig['blacklist']

	def filterIv(self, pokemon):
		pokemonIv = getFullStats(pokemon.atkIv, pokemon.defIv, pokemon.staIv)
		maxIv = int(self.filterConfig['ivMax'])
		minIv = int(self.filterConfig['ivMin'])
		return pokemonIv <= maxIv and pokemonIv >= minIv and pokemon.pokemonId not in self.filterConfig['blacklist']

	def filterWhiteListIv(self, pokemon):
		pokemonIv = getFullStats(pokemon.atkIv, pokemon.defIv, pokemon.staIv)
		maxIv = int(self.filterConfig['ivMax'])
		minIv = int(self.filterConfig['ivMin'])
		return pokemonIv <= maxIv and pokemonIv >= minIv and pokemonId in self.filterConfig['whitelist'] and pokemon.pokemonId not in self.filterConfig['blacklist']