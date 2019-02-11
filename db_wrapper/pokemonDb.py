import connector


def getPokemon():
	databaseObj = connector.DatabaseConnector()
	cnx = databaseObj.connect()

	cursor = cnx.cursor(dictionary=True)
	allVisiblePokemon = ("SELECT * FROM pokemon WHERE disappear_time > CONVERT_TZ(NOW(), @@session.time_zone, '+00:00');")
	cursor.execute(allVisiblePokemon)
	result_set = cursor.fetchall()

	cursor.close()
	cnx.close()

	return result_set
