#!/usr/bin/env python
# coding: utf8

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from pokemon_data import *
import json
import time

from datetime import datetime
import datetime as dt

def parseGeofence(geofenceFilePath):
	if (geofenceFilePath == ""):
		return False
	with open(geofenceFilePath, 'r') as f:
		geofence = f.read()
		# empty array for polygon
		polygon_array = []
		# first split the point into tuple array
		points = geofence.split(";")

		for point in points:
			splitted_point = point.split(",")
			if len(splitted_point) == 2:
				point_tuple = (float(splitted_point[0]),float(splitted_point[1]))
				polygon_array.append(point_tuple)
		return Polygon(polygon_array)

def isInGeofence(geofence, pokemon):
	if (not geofence):
		return True
	else:
		return geofence.contains(Point(pokemon['latitude'],pokemon['longitude']))

def isNotInGeofence(geofence, pokemon):
	if (not geofence):
		return True
	else:
		return not geofence.contains(Point(pokemon['latitude'],pokemon['longitude']))

def getGender(gender):
	if gender== 1:
		return "♂"
	elif gender == 2:
		return "♀"
	return ""

def getWeather(weather_cond):
	if weather_cond is None:
		weather_cond = 0
	return weather_emojis[str(weather_cond)]

def getForm(pokemon_id, form):
	if pokemon_id == 201:
		return "Form: " + alphabet[form] + "\n"
	else:
		return ""

def getFullStats (pokemon):
	if pokemon['individual_attack'] is None:
		return -1
	else:
		return pokemon['individual_attack'] + pokemon['individual_defense'] + pokemon['individual_stamina']

def calcIV (iv_a, iv_d, iv_s):
	i = (iv_a + iv_d + iv_s) * 100 / 45
	return round(i)

def getPokemonLevel(cpMultiplier):
	if cpMultiplier < 0.734:
		pokemonLevel = (58.35178527 * cpMultiplier * cpMultiplier - 2.838007664 * cpMultiplier + 0.8539209906)
	else:
		pokemonLevel = 171.0112688 * cpMultiplier - 95.20425243

	pokemonLevel = (round(pokemonLevel) * 2) / 2

	return pokemonLevel

# returns the dissapear time in human readable H/M/S format
def getDisapearTime(disappear_time):
	disappear_time = disappear_time + dt.timedelta(hours=1)
	return disappear_time.time()

# returns a string "MMm SSs"
def getPokemonDurationTime(disappear_time):
	duration = ( disappear_time + dt.timedelta(hours=1) ) - dt.datetime.now()
	totsec = duration.total_seconds()
	if(totsec > 0):
		m = (totsec%3600) // 60
		sec =(totsec%3600)%60
		return "{:02d}m {:02d}s".format(int(m), int(sec))
	else:
		return "{:02d}m {:02d}s".format(int(0), int(0))

def checkIfSpawnIsExpired(disappear_time):
	duration = ( disappear_time + dt.timedelta(hours=1) ) - dt.datetime.now()
	totsec = duration.total_seconds()
	if(totsec > 0):
		return False
	else:
		return True
