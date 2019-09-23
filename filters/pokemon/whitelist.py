#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter

class Whitelist(BaseFilter):

    def __init__(self, filterConfig):
        super(Whitelist, self).__init__(filterConfig, 'mon_whitelist')

    def isSatisfied(self, pokemon):
		  return pokemon.pokemonId in self.filterConfig['whitelist'] and pokemon.pokemonId not in self.filterConfig['blacklist']
        
    
    def testConfig(self):
        # test if a whitelist is set
        if('whitelist' not in self.filterConfig):
            raise ValueError("Missing Field \"whitelist\" in filter configuration. Please provide a valid filter configuration for mon_whitelist.")
        
        whitList = self.filterConfig['whitelist']
        
        # test if the whitelist has at least one pokemon
        if(len(whitList) == 0):
            raise ValueError("The whitelist is empty. Please provide at least one Pokemon Id. ")
        
        self.logger.info("Filter config for whitelist is fine.")
