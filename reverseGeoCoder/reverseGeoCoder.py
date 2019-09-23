#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json 
import time
import logging


class ReverseGeoCoder:
    
    url_base = "https://maps.googleapis.com/maps/api/geocode/json?"
    cleanUpBufferTimeInternal = 0 # default 43200 seconds / 12h

    requestBuffer = {}

    def __init__(self, googleApiKey, cleanUpBufferTimeInternal=43200, maxBufferSize = 100):

        logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # google api key
        self.googleApiKey = googleApiKey                
        # auto clean action after X minutes clean buffer
        self.cleanUpBufferTimeInternal = cleanUpBufferTimeInternal
        # max size from buffer
        self.maxBufferSize = maxBufferSize

        # lets test the api key
        self.testApiKey()


    def testApiKey(self):
        # lat/lon LA
        la_lat =  34.052235
        la_lon = -118.243683
        
        self.logger.info("Test google maps api key")

        resp = self.askGoogle(la_lat, la_lon)
        if (resp['status'] == 'OK'):
			self.logger.info("google api key is fine")
        else:
            self.logger.error("Something went wrong with yout google api key.")
            self.logger.error("Reponse status: %s",resp['status'])
            self.logger.error("Reponse message: %s",resp['error_message'])
            exit()

    # Send request to google reverse gecoding api
    def askGoogle(self, lat, lon):
        params = "latlng={lat},{lon}&key={key}".format(
            lat=lat,
            lon=lon,
            key=self.googleApiKey
        )
        url = "{url_base}{params}".format(url_base=self.url_base, params=params)
        res_ob = requests.get(url)
        x = res_ob.json() 
        return x 

    # add response to buffer as hash(lat, lon)
    def addRequestToBuffer(self, lat, lon, response):
        hashKey = self._getHash(lat,lon)
        self.requestBuffer[hashKey] = {'response' : response , 'timestamp' : time.time()} 

    # function that checks the buffer and than google
    def search(self, lat, lon):
        hashKey = self._getHash(lat,lon)
        if(hashKey in self.requestBuffer):
            print ("Request found in Buffer")
            return self.requestBuffer[hashKey]['response']
        else:
            print ("No Request found, so i ask google")
            resp = self.askGoogle(lat, lon)
            
            # add only valid requests
            if (resp['status'] == 'OK'):
                self.addRequestToBuffer(lat, lon, resp)
                return resp
            else: 
                print (resp)
                return False 

    # helper funtion to generate hash
    def _getHash(self, lat, lon):
        return hash((lat, lon))


    def _cleanBufferInternal(self):
        
        print ("Delete all Request from Buffer older than: " + str(self.cleanUpBufferTimeInternal) + " seconds")
        deletedEntries = 0
        for entry in self.requestBuffer.keys():
            if(self.requestBuffer[entry]['timestamp'] + self.cleanUpBufferTimeInternal  < time.time()):
                del self.requestBuffer[entry]
                deletedEntries = deletedEntries + 1

        print ("CleanUp action is done. A total of " + str(deletedEntries) + " Request is deleted...")

    # clean the buffer with all response that are olderThan X
    # must be call manual
    def cleanBuffer(self, olderThan):
        
        print ("Delete all Request from Buffer older than: " + str(olderThan) + " seconds")
        deletedEntries = 0
        for entry in self.requestBuffer.keys():
            if(self.requestBuffer[entry]['timestamp'] + olderThan  < time.time()):
                del self.requestBuffer[entry]
                deletedEntries = deletedEntries + 1

        print ("CleanUp action is done. A total of " + str(deletedEntries) + " Request is deleted...")


"""
def test():
    
    rgc =  ReverseGeoCoder("")
   
    print(rgc.search("49.49671", "8.47955")['results'][0]['formatted_address']) 
    print(rgc.search("49.49571", "8.47956")['results'][0]['formatted_address']) 
    print(rgc.search("49.44671", "8.47956")['results'][0]['formatted_address']) 
    time.sleep(5)
    print(rgc.search("49.42671", "8.47956")['results'][0]['formatted_address']) 
    print(rgc.search("49.49371", "8.47956")['results'][0]['formatted_address']) 

    print(len(rgc.requestBuffer))
    rgc.cleanBuffer(5)
    print(len(rgc.requestBuffer))
 
    print(rgc.search("49.49671", "8.47955")['results'][0]['formatted_address']) 
    print(rgc.search("49.49571", "8.47956")['results'][0]['formatted_address']) 
    print(rgc.search("49.44671", "8.47956")['results'][0]['formatted_address']) 
    print(rgc.search("49.42671", "8.47956")['results'][0]['formatted_address']) 
    print(rgc.search("49.49371", "8.47956")['results'][0]['formatted_address']) 


   

test()
"""