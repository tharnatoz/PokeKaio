#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter
from filters import helper

class Mon_Iv(BaseFilter):

    def __init__(self, filterConfig):
        super(Mon_Iv, self).__init__(filterConfig)

    def isSatisfied(self, pokemon):

        if(pokemon.atkIv is None):
            return False
        
        pokemonIv = pokemon.atkIv + pokemon.defIv+pokemon.staIv
        maxIv = int(self.filterConfig['ivMax'])
        minIv = int(self.filterConfig['ivMin'])
        return pokemonIv <= maxIv and pokemonIv >= minIv and pokemon.pokemonId not in self.filterConfig['blacklist']
        
    
    def testConfig(self):

        # test if a maxIv is set
        helper.hasOwnProperty(self.filterConfig, 'ivMax')

        # test if a minIv is set
        helper.hasOwnProperty(self.filterConfig, 'ivMin')
        
        # test if is value is numeric if its provided as string
        helper.isStringDigit(self.filterConfig, 'ivMax')
        helper.isStringDigit(self.filterConfig, 'ivMin')

        # at this point we know the ivMax and ivMin value are mumeric and can cast to integer        
        ivMax = int(self.filterConfig['ivMax'])
        ivMin = int(self.filterConfig['ivMin'])
        
        # ivMax/ivMin is between 0 and 45
        helper.checkIfValueIsInRange(ivMax, 0, 45, 'ivMax', self.filterConfig['name'])
        helper.checkIfValueIsInRange(ivMin, 0, 45, 'ivMin', self.filterConfig['name'])

        # ivMax must greater than ivMin
        helper.minMaxIvRangeCorrect(ivMin, ivMax, self.filterConfig['name'])

        # test if a blacklist is set
        helper.testBlackList(self.filterConfig)
        
        self.logger.info("Filter config for "+self.filterType +" is fine.")
