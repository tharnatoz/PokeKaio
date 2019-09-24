#!/usr/bin/env python
# coding: utf8

import mysql.connector
from mysql.connector import errorcode

from utils import utils
from utils import configParser as cp

class DatabaseConnector:

	def __init__(self, config):
		# get database config
		self.user = 	config['user']
		self.password = config['password']
		self.host = 	config['host']
		self.database = config['name']
		self.port = 	config['port']

	def connect(self):

		try:
			cnx = mysql.connector.connect(	user = self.user,
											password = self.password,
        	    	                  		host = self.host,
            	    	              		database = self.database,
            	    	              		port = self.port)
		except mysql.connector.Error as err:
  			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
		else:
			return cnx

