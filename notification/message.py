#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import utils as u
from pokemon_data import *

def getMessage(pokemon):
	if pokemon.atkIv is not None:
		return getMessageWithMonInfos(pokemon)
	else:
		return getMessageWithoutMonInfos(pokemon)

def getMessageWithMonInfos(pokemon):
	pokemon_id = pokemon.pokemonId
	form = pokemon.form
	iv_a = pokemon.atkIv
	iv_d = pokemon.defIv
	iv_s = pokemon.staIv
	gender = pokemon.gender
	cp = pokemon.cp
	weather = pokemon.weather

	lv = str(pokemon.level)
	full_iv = pokemon.iv
	duration = pokemon.duration
	disappear_time = pokemon.disappear_time

	expireTimestampVerified = _getSpawnpointValidationInfo(pokemon)

	message ="<b>Ein wildes " + pokemons_de[pokemon_id]+gender+"</b>"+ weather +"\n"+str(form)+	str(cp) +"WP - "+str(full_iv)+"%IV - LVL "+lv+"\n"+"(A"+str(iv_a)+"/D"+str(iv_d)+"/S"+str(iv_s)+") \n"+	"Noch " + str(duration) + " bis " + str(disappear_time) + "Uhr\n"+expireTimestampVerified

	return message


def getMessageWithoutMonInfos(pokemon):
	pokemon_id = pokemon.pokemonId
	form = pokemon.form
	gender = pokemon.gender
	weather = pokemon.weather
	duration = pokemon.duration
	disappear_time = pokemon.disappear_time
	expireTimestampVerified = _getSpawnpointValidationInfo(pokemon)

	message = "<b>Ein wildes " + pokemons_de[pokemon_id]+gender+"</b>"+ weather +"\n"+str(form)+ "Noch " + str(duration) + " bis " + str(disappear_time) + "Uhr\n"+expireTimestampVerified

	return message

def _getSpawnpointValidationInfo(pokemon):
	expireTimestampVerified = pokemon.expireTimestampVerified
	
	# not available
	if expireTimestampVerified == -1:
		return " "
	# verified
	if expireTimestampVerified == True:
		return "<b>Die Zeit ist richtig! Let's Go!</b>"

	# not verified
	if expireTimestampVerified == False:
		return "<b>Risky! Die Zeit ist eine Schätzung.</b>"