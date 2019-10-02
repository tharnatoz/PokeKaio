#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter
from filters import helper

class Mon_Stats(BaseFilter):

    def __init__(self, filterConfig):
        super(Mon_Stats, self).__init__(filterConfig, 'mon_stats')

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
        helper.hasOwnProperty(self.filterConfig, 'iVmaxAtk')

        # test if a f_monDef is set
        helper.hasOwnProperty(self.filterConfig, 'iVminDef')

        # test if a f_monSta is set
        helper.hasOwnProperty(self.filterConfig, 'iVminSta')

        # test if a f_monCP is set
        helper.hasOwnProperty(self.filterConfig, 'maxCP')

         # test if is value is numeric if its provided as string
        helper.isStringDigit(self.filterConfig, 'iVmaxAtk')
        helper.isStringDigit(self.filterConfig, 'iVminDef')
        helper.isStringDigit(self.filterConfig, 'iVminSta')
        helper.isStringDigit(self.filterConfig, 'maxCP')

        # at this point we know the ivMax and ivMin value are mumeric and can cast to integer
        f_monAtk = int(self.filterConfig['iVmaxAtk'])
        f_monDef = int(self.filterConfig['iVminDef'])
        f_monSta = int(self.filterConfig['iVminSta'])

        # iVmaxAtk is between 0 and 15
        helper.checkIfValueIsInRange(f_monAtk, 0, 15, 'iVmaxAtk', self.filterConfig['name'])

        # ivMin is between 0 and 15
        helper.checkIfValueIsInRange(f_monDef, 0, 15, 'iVminDef', self.filterConfig['name'])

        # ivMin is between 0 and 15
        helper.checkIfValueIsInRange(f_monSta, 0, 15, 'iVminSta', self.filterConfig['name'])

        # test if a blacklist is set
        helper.testBlackList(self.filterConfig)

        self.logger.info("Filter config for  "+self.filterType +" is fine.")
