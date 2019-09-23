#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter

class Mon_Iv(BaseFilter):

    def __init__(self, filterConfig):
        super(Mon_Iv, self).__init__(filterConfig, 'mon_iv')

    def isSatisfied(self, pokemon):

        if(pokemon.atkIv is None):
            return False
        
        pokemonIv = pokemon.atkIv + pokemon.defIv+pokemon.staIv
        maxIv = int(self.filterConfig['ivMax'])
        minIv = int(self.filterConfig['ivMin'])
        return pokemonIv <= maxIv and pokemonIv >= minIv and pokemon.pokemonId not in self.filterConfig['blacklist']
        
    
    def testConfig(self):
        # test if a maxIv is set
        if('ivMax' not in self.filterConfig):
            raise ValueError("Missing Field \"maxIv\" in filter configuration. Please provide a valid filter configuration for "+self.filterType +".")
        
        # test if a minIv is set
        if('ivMin' not in self.filterConfig):
            raise ValueError("Missing Field \"minIv\" in filter configuration. Please provide a valid filter configuration for "+self.filterType +".")
        
        # cast to string
        ivMax = str(self.filterConfig['ivMax'])
        ivMin = str(self.filterConfig['ivMin'])

        # ivMax is digit?
        if(not ivMax.isdigit()):
            raise ValueError("ivMax Value Error. Allowed Valure are 0-45. Please check your maxIv settings in "+self.filterType +".")
        # ivMin is digit?
        if(not ivMin.isdigit()):
            raise ValueError("ivMin Value Error. Allowed Valure are 0-45. Please check your minIv settings in "+self.filterType +".")
        # ivMax is between 0 and 45
        if(isinstance(ivMax, int) and ivMax >45 or ivMax < 0):
            raise ValueError("ivMax Value Error. Allowed Valure are 0-45. Please check your maxIv settings in "+self.filterType +".")
        # ivMin is between 0 and 45
        if(isinstance(ivMin, int) and ivMin >45 or ivMin < 0):
            raise ValueError("ivMin Value Error. Allowed Valure are 0-45. Please check your minIv settings in "+self.filterType +".")
        # ivMax must greate than ivMin
        if(ivMin > ivMax):
            raise ValueError("The minIv is greate than the maxIv. Please check your settings in "+self.filterType +" filter")
        # test if a blacklist is set
        if('blacklist' not in self.filterConfig):
            raise ValueError("Missing Field \"blacklist\" in filter configuration. Please provide at least an empty blacklist in "+self.filterType +" filter.")
        
        self.logger.info("Filter config for "+self.filterType +" is fine.")
