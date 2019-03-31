from utils import utils as u
from pokemon_data import *

def getMessage(pokemon):
	if pokemon.atkIv is not None:
		return getMessageWithMonInfos(pokemon)
	else:
		return getMessageWithotMonInfos(pokemon)

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
	duration = pokemon.disappear_time
	disappear_time = pokemon.disappear_time

	message ="<b>Ein wildes " + pokemons_de[pokemon_id]+gender+"</b>"+ weather +"\n"+str(form)+	str(cp) +"WP - "+str(full_iv)+"%IV - LVL "+lv+"\n"+"(A"+str(iv_a)+"/D"+str(iv_d)+"/S"+str(iv_s)+") \n"+	"Noch " + str(duration) + " bis " + str(disappear_time) + "Uhr"

	return message


def getMessageWithotMonInfos(pokemon):
	pokemon_id = pokemon.pokemonId
	form = pokemon.form
	gender = pokemon.gender
	weather = pokemon.weather
	duration = pokemon.disappear_time
	disappear_time = pokemon.disappear_time

	message = "<b>Ein wildes " + pokemons_de[pokemon_id]+gender+"</b>"+ weather +"\n"+str(form)+ "Noch " + str(duration) + " bis " + str(disappear_time) + "Uhr"

	return message


