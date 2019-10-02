#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter
from filters import helper

class Mon_Advanced_Stats(BaseFilter):

    def __init__(self, filterConfig):
        super(Mon_Advanced_Stats, self).__init__(filterConfig, 'mon_advanced_stats')

    def isSatisfied(self, pokemon):

        if(pokemon.atkIv is None):
            return False

        for monFilter in self.filterConfig['mons']:
            if pokemon.pokemonId == monFilter['monId']:
                # now test values
                return self.testValue(pokemon.atkIv, monFilter['ivAtk']) and self.testValue(pokemon.defIv, monFilter['ivDef']) and self.testValue(pokemon.staIv, monFilter['ivSta']) and self.testValue(pokemon.cp, monFilter['cp'])


    # test the found pokemon value against the filter condition 
    def testValue(self, foundValue, filterCondition):
        splitted = filterCondition.split(':')
        condFilter = splitted[0]
        valFilter = int(splitted[1])
        if(condFilter == "=="):
            return foundValue == valFilter
        if(condFilter == ">="):
            return foundValue >= valFilter
        if(condFilter == "<="):
            return foundValue <= valFilter
    

    def testConfig(self):
        for monFilter in self.filterConfig['mons']:
            # tmp filter name for improved error finding
            tmpFilterName = self.filterType +" mon-id- "+str(monFilter['monId'])
            
            # now check if all properties are set in each advanced mon filter
            helper.hasOwnProperty(monFilter,'monId', tmpFilterName)
            helper.hasOwnProperty(monFilter,'ivAtk', tmpFilterName)
            helper.hasOwnProperty(monFilter,'ivDef', tmpFilterName)
            helper.hasOwnProperty(monFilter,'ivSta', tmpFilterName)
            helper.hasOwnProperty(monFilter,'cp',    tmpFilterName)

            # check for each stat/cp it condition and value is set
            helper.checkIfConditionAndValueIsSet(monFilter['ivAtk'], tmpFilterName)
            helper.checkIfConditionAndValueIsSet(monFilter['ivDef'], tmpFilterName)
            helper.checkIfConditionAndValueIsSet(monFilter['ivSta'], tmpFilterName)
            helper.checkIfConditionAndValueIsSet(monFilter['cp'],    tmpFilterName)

            # first split the filter
            splittedAtk =  monFilter['ivAtk'].split(':')
            splittedDef =  monFilter['ivDef'].split(':')
            splittedSta =  monFilter['ivSta'].split(':')
            splittedCp =   monFilter['cp'].split(':')

            # extract the condition, allowed values are ==, >=, <=
            condFilterAtk = splittedAtk[0]
            condFilterDef = splittedDef[0]
            condFilterSta = splittedSta[0]
            condFilterCp =  splittedCp[0]
            
            # now check if all properties are set in each advanced mon filter
            helper.checkAdvancedMonFilterCondition(condFilterAtk, tmpFilterName)
            helper.checkAdvancedMonFilterCondition(condFilterDef, tmpFilterName)
            helper.checkAdvancedMonFilterCondition(condFilterSta, tmpFilterName)
            helper.checkAdvancedMonFilterCondition(condFilterCp , tmpFilterName)

            # extract the condition value, must be in range 0-15
            valueFilterAtk = int(splittedAtk[1])
            valueFilterDef = int(splittedDef[1])
            valueFilterSta = int(splittedSta[1])

            # now check if the stats are >=0 and <=15
            helper.checkIfValueIsInRange(valueFilterAtk, 0, 15, "ivAtk", tmpFilterName)
            helper.checkIfValueIsInRange(valueFilterDef, 0, 15, "ivDef", tmpFilterName)
            helper.checkIfValueIsInRange(valueFilterSta, 0, 15, "ivSta", tmpFilterName)

        self.logger.info("Filter config for "+ self.filterType +" is fine.")
