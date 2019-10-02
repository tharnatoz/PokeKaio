#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter
from filters import helper

class Mon_Whitelist(BaseFilter):

    def __init__(self, filterConfig):
        super(Mon_Whitelist, self).__init__(filterConfig, 'mon_whitelist')

    def isSatisfied(self, pokemon):
        return pokemon.pokemonId in self.filterConfig['whitelist'] and pokemon.pokemonId not in self.filterConfig['blacklist']
        
    
    def testConfig(self):
        
        # whitelist test
        helper.testWhiteList(self.filterConfig)

        # test if a blacklist is set
        helper.testBlackList(self.filterConfig)
        
        self.logger.info("Filter config for  "+self.filterType +" is fine.")
