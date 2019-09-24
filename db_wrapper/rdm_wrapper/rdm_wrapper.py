#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db_wrapper.baseWrapper import BaseWrapper
import time

from model import pokemon as pokemon_model
from model import raid as raid_model
from model import quest as quest_model

from utils import utils as u

class RdmWrapper(BaseWrapper):

    def __init__(self, config):

		# set last db request time
        self.lastDatabaseRequestTime = time.time()

        super(RdmWrapper, self).__init__(config)


    def getPokemonData(self, raw=False):
		try:
            # get connction
			cnx = self.databaseConnector.connect()

			cursor = cnx.cursor(dictionary=True)
			query_allVisiblePokemon = ("SELECT from_unixtime(expire_timestamp) AS disappear_time, id, pokemon_id, form, atk_iv, def_iv, sta_iv, gender, cp, weather, lat, lon, iv, level, expire_timestamp_verified FROM pokemon WHERE updated >" + str(self.lastDatabaseRequestTime) +";")
			cursor.execute(query_allVisiblePokemon)
			result_set = cursor.fetchall()

			cursor.close()
			cnx.close()

			# remember request time
			self.lastDatabaseRequestTime = time.time()

			# raw data or parsed data?
			if(raw):
				return result_set
			else:
				pokemons = self.parsePokemonDataToModel(result_set)
				return pokemons
				
		except Exception as e:
			print (e)
			pokemons = []
		
		return pokemons 

    def getRaidData(self, raw=False):
        pass 

    def getQuestData(self,raw=False):
        pass 
    
    def parsePokemonDataToModel(self, rawData):
        # pokemon list
		pokemons = []
		
		for pokemon_relation in rawData:

			pokemon = pokemon_model.Pokemon()

			pokemon.encounterId = pokemon_relation['id']
			pokemon.pokemonId = pokemon_relation['pokemon_id']
			pokemon.lat = pokemon_relation['lat']
			pokemon.lon = pokemon_relation['lon']
			pokemon.iv = pokemon_relation['iv']
			pokemon.atkIv = pokemon_relation['atk_iv']
			pokemon.defIv = pokemon_relation['def_iv']
			pokemon.staIv = pokemon_relation['sta_iv']
			pokemon.form = u.getForm(pokemon.pokemonId , pokemon_relation['form'])
			pokemon.gender = u.getGender(pokemon_relation['gender'])
			pokemon.weather = u.getWeather(pokemon_relation['weather'])
			pokemon.level = pokemon_relation['level']
			pokemon.cp = pokemon_relation['cp']
			pokemon.disappear_timestamp = pokemon_relation['disappear_time']
			pokemon.disappear_time = u.getDisapearTime(pokemon_relation['disappear_time'])
			pokemon.duration = u.getPokemonDurationTime(pokemon_relation['disappear_time'])
			pokemon.expireTimestampVerified = pokemon_relation['expire_timestamp_verified']

			# add pokemon to list
			pokemons.append(pokemon)

		return pokemons

    def parseRaidDataToModel(self, rawData):   
        pass 

    def parseQuestDataToModel(self, rawData):
        pass 