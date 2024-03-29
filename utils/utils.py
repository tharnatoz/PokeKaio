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

def isInGeofence(geofence, lat, lon):
	if (not geofence):
		return True
	else:
		return geofence.contains(Point(lat, lon))

def isNotInGeofence(geofence, lat, lon):
	if (not geofence):
		return True
	else:
		return not geofence.contains(Point(lat, lon))

def getGender(gender):
	if gender == 1:
		return "♂"
		#return u'\u2642'  # male symbol
	elif gender == 2:
		return "♀"
		#return u'\u2640'  # female symbol
	elif gender == 3:
		return "⚲"
		#return u'\u26b2'  # neutral
	return ''  


def getWeather(weather_cond):
	if weather_cond is None:
		weather_cond = 0
	return weather_emojis[str(weather_cond)]

def getForm(pokemon_id, form):
	if pokemon_id == 201:
		return "Form: " + alphabet[form] + "\n"
	else:
		return ""

def calcIV (iv_a, iv_d, iv_s):
	if iv_a is None:
		return -1
	i = (iv_a + iv_d + iv_s) * 100 / 45
	return round(i)

def getPokemonLevel(cpMultiplier):
	if cpMultiplier is None:
		return -1
	if cpMultiplier < 0.734:
		pokemonLevel = (58.35178527 * cpMultiplier * cpMultiplier - 2.838007664 * cpMultiplier + 0.8539209906)
	else:
		pokemonLevel = 171.0112688 * cpMultiplier - 95.20425243

	pokemonLevel = (round(pokemonLevel) * 2) / 2

	return pokemonLevel

# returns the dissapear time in human readable H/M/S format
def getDisapearTime(disappear_time):
	return disappear_time.time()

# returns a string "MMm SSs"
def getPokemonDurationTime(disappear_time):
	duration = disappear_time - dt.datetime.now()
	totsec = duration.total_seconds()
	if(totsec > 0):
		m = (totsec%3600) // 60
		sec =(totsec%3600)%60
		return "{:02d}m {:02d}s".format(int(m), int(sec))
	else:
		return "{:02d}m {:02d}s".format(int(0), int(0))

def checkIfSpawnIsExpired(disappear_time):
	duration = disappear_time - dt.datetime.now()
	totsec = duration.total_seconds()
	if(totsec > 0):
		return False
	else:
		return True

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset
