from utils import utils as u
from pokemon_data import *

def getMessage(pokemon):
	if pokemon["individual_attack"] is not None:
		return getMessageWithMonInfos(pokemon)
	else:
		return getMessageWithotMonInfos(pokemon)

def getMessageWithMonInfos(pokemon):
	pokemon_id = pokemon["pokemon_id"]
	form = u.getForm(pokemon_id,pokemon["form"])
	iv_a = pokemon["individual_attack"]
	iv_d = pokemon["individual_defense"]
	iv_s = pokemon["individual_stamina"]
	gender = u.getGender(pokemon["gender"])
	cp = pokemon["cp"]
	weather = u.getWeather(pokemon["weather_boosted_condition"])
	lv = str(u.getPokemonLevel(pokemon['cp_multiplier']))
	full_iv = u.calcIV(iv_a, iv_d, iv_s)
	duration = u.getPokemonDurationTime(pokemon["disappear_time"])
	disappear_time = u.getDisapearTime(pokemon["disappear_time"])

	message ="<b>Ein wildes " + pokemons_de[pokemon_id]+gender+"</b>"+ weather +"\n"+str(form)+	str(cp) +"WP - "+str(full_iv)+"%IV - LVL "+lv+"\n"+"(A"+str(iv_a)+"/D"+str(iv_d)+"/S"+str(iv_s)+") \n"+	"Noch " + str(duration) + " bis " + str(disappear_time) + "Uhr"
	return message


def getMessageWithotMonInfos(pokemon):
	pokemon_id = pokemon["pokemon_id"]
	form = u.getForm(pokemon_id,pokemon["form"])
	gender = u.getGender(pokemon["gender"])
	weather = u.getWeather(pokemon["weather_boosted_condition"])
	duration = u.getPokemonDurationTime(pokemon["disappear_time"])
	disappear_time = u.getDisapearTime(pokemon["disappear_time"])

	message = "<b>Ein wildes " + pokemons_de[pokemon_id]+gender+"</b>"+ weather +"\n"+str(form)+ "Noch " + str(duration) + " bis " + str(disappear_time) + "Uhr"

	return message


