
import connector
from utils.utils import  getLastModifiedTime
from utils.utils import  getLastModifiedTime_lowest

def getPokemon():
	databaseObj = connector.DatabaseConnector()
	cnx = databaseObj.connect()

	last_modified_time = getLastModifiedTime()
	last_modified_time_lowest = getLastModifiedTime_lowest()

	cursor = cnx.cursor(dictionary=True)
	allAccountsQuery = ("SELECT * FROM pokemon where last_modified > %s and individual_attack is not Null OR (last_modified < %s and last_modified > %s)ORDER BY  last_modified DESC;")
	queryData = (last_modified_time, last_modified_time, last_modified_time_lowest)
	cursor.execute(allAccountsQuery, queryData)
	result_set = cursor.fetchall()

	cursor.close()
	cnx.close()

	return result_set

def getPokemonsByIvRange():
	return

def getPokemonsByWhitelist():
	return