#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter

class Mon_Stats(BaseFilter):

    def __init__(self, filterConfig):
        super(Mon_Stats, self).__init__(filterConfig, 'mon_whitelist')

    def isSatisfied(self, pokemon):
        if (pokemon.atkIv is None):
            return False

        f_monAtk = int(self.filterConfig['iVmaxAtk'])
        f_monDef = int(self.filterConfig['iVminDef'])
        f_monSta = int(self.filterConfig['iVminSta'])
        f_monCP = int(self.filterConfig['maxCP'])

        return pokemon.atkIv <= f_monAtk and pokemon.defIv >= f_monDef and pokemon.staIv >= f_monSta and pokemon.cp <= f_monCP and pokemon.pokemonId not in self.filterConfig['blacklist']
        
    
    def testConfig(self):
       
        # test if a iVmaxAtk is set
        if('iVmaxAtk' not in self.filterConfig):
            raise ValueError("Missing Field \"iVmaxAtk\" in filter configuration. Please provide a valid filter configuration for "+self.filterType +".")
        
        # test if a f_monDef is set
        if('iVminDef' not in self.filterConfig):
            raise ValueError("Missing Field \"iVminDef\" in filter configuration. Please provide a valid filter configuration for "+self.filterType +".")
        
        # test if a f_monSta is set
        if('iVminSta' not in self.filterConfig):
            raise ValueError("Missing Field \"iVminSta\" in filter configuration. Please provide a valid filter configuration for "+self.filterType +".")
        
        # test if a f_monCP is set
        if('maxCP' not in self.filterConfig):
            raise ValueError("Missing Field \"maxCP\" in filter configuration. Please provide a valid filter configuration for "+self.filterType +".")

        # cast to string
        f_monAtk = str(self.filterConfig['iVmaxAtk'])
        f_monDef = str(self.filterConfig['iVminDef'])
        f_monSta = str(self.filterConfig['iVminSta'])
        f_monCP = str(self.filterConfig['maxCP'])


        # ivMax is digit?
        if(not f_monAtk.isdigit()):
            raise ValueError("iVmaxAtk Value Error. Allowed Valure are 0-15. Please check your iVmaxAtk settings in "+self.filterType +".")
        # ivMin is digit?
        if(not f_monDef.isdigit()):
            raise ValueError("iVminDef Value Error. Allowed Valure are 0-15. Please check your iVminDef settings in "+self.filterType +".")
        # ivMax is digit?
        if(not f_monSta.isdigit()):
            raise ValueError("iVminSta Value Error. Allowed Valure are 0-15. Please check your iVminSta settings in "+self.filterType +".")
        # ivMin is digit?
        if(not f_monCP.isdigit()):
            raise ValueError("maxCP Value Error. Allowed Valure are digits [0-9]. Please check your maxCP settings in "+self.filterType +".")
        
        
        # iVmaxAtk is between 0 and 15
        if(isinstance(f_monAtk, int) and f_monAtk >15 or f_monAtk < 0):
            raise ValueError("ivMax Value Error. Allowed Valure are 0-15. Please check your iVmaxAtk settings in "+self.filterType +".")
        # ivMin is between 0 and 15
        if(isinstance(f_monDef, int) and f_monDef >15 or f_monDef < 0):
            raise ValueError("iVminDef Value Error. Allowed Valure are 0-15. Please check your iVminDef settings in "+self.filterType +".")
            # ivMin is between 0 and 15
        if(isinstance(f_monSta, int) and f_monSta >15 or f_monSta < 0):
            raise ValueError("ivMin Value Error. Allowed Valure are 0-15. Please check your iVminSta settings in "+self.filterType +".")
        
        # test if a blacklist is set
        if('blacklist' not in self.filterConfig):
            raise ValueError("Missing Field \"black\" in filter configuration. Please provide at least an empty blacklist in mon_whitelist.")
        
        self.logger.info("Filter config for mon_whitelist is fine.")
