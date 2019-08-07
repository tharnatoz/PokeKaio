#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json 
import time

class ReverseGeoCoder:
    
    url_base = "https://maps.googleapis.com/maps/api/geocode/json?"
    cleanUpBufferTimeInternal = 0 # default 3600 seconds

    requestBuffer = {}

    def __init__(self, googleApiKey, cleanUpBufferTimeInternal=3600):
        self.googleApiKey = googleApiKey                
        self.cleanUpBufferTimeInternal = cleanUpBufferTimeInternal                                                             


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


    def addRequestToBuffer(self, lat, lon, response):
        hashKey = self._getHash(lat,lon)
        self.requestBuffer[hashKey] = {'response' : response , 'timestamp' : time.time()} 

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
                print resp
                return False 

    def _getHash(self, lat, lon):
        return hash((lat, lon))

    def _cleanBufferInternal(self):
        
        print "Delete all Request from Buffer older than: " + str(self.cleanUpBufferTimeInternal) + " seconds"
        deletedEntries = 0
        for entry in self.requestBuffer.keys():
            if(self.requestBuffer[entry]['timestamp'] + self.cleanUpBufferTimeInternal  < time.time()):
                del self.requestBuffer[entry]
                deletedEntries = deletedEntries + 1

        print "CleanUp action is done. A total of " + str(deletedEntries) + " Request is deleted..."

    def cleanBuffer(self, olderThan):
        
        print "Delete all Request from Buffer older than: " + str(olderThan) + " seconds"
        deletedEntries = 0
        for entry in self.requestBuffer.keys():
            if(self.requestBuffer[entry]['timestamp'] + olderThan  < time.time()):
                del self.requestBuffer[entry]
                deletedEntries = deletedEntries + 1

        print "CleanUp action is done. A total of " + str(deletedEntries) + " Request is deleted..."



def main():
    
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


   

main()