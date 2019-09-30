#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class MessageParser():

    def __init__(self, locale, messenger):
        self.locale = locale
        self.messenger = messenger

        # load messages.json - default
        with open('message/lang/{}/messages.json'.format(self.locale)) as f:
            self.messages = json.load(f)
        
        # load pokemon.json - default
        with open('message/lang/{}/pokemon.json'.format(self.locale)) as f:
            self.pokemon = json.load(f)

    
    # replace the placeholder with the infos  
    def replace(self, string, infDict):
        if string is None:
            return None
        s = string.encode('UTF-8')
        for key in infDict:
            s = s.replace("{"+key+"}", str(infDict[key]))
        
        # now replace the pokemon name if a mon id is set in dict
        if('pokemonId' in infDict):
            pName = self.getPokemonName(infDict['pokemonId']) 
            s = s.replace("{pokemonName}", pName)
        
        return s
    
    # returns the message utf-8 encoded
    def getMessage(self, key):
        s = self.messages[self.messenger][key]
        string = s.encode('UTF-8')
        return string

    def getPokemonName(self, id):
        if(id > 0 and id < len(self.pokemon['name'])-1):
            s = self.pokemon['name'][id]
            string = s.encode('UTF-8')
            return string
        else:
            return "No name found"