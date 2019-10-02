#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.baseFilter import BaseFilter
from filters import helper

class Mon_Advanced(BaseFilter):

    def __init__(self, filterConfig):
        super(Mon_Advanced, self).__init__(filterConfig)

    def isSatisfied(self, pokemon):

        if(pokemon.atkIv is None):
            return False

        for monFilter in self.filterConfig['mons']:
            # first check pokemon id
            if pokemon.pokemonId != monFilter['monId']:
                return False
            # gender
            if "gender" in monFilter:
                # pokemon male - filter female -> !=
                if pokemon.gender == 1 and monFilter['gender'] == 'f':
                    return False
                # pokemon female - filter male -> != 
                if pokemon.gender == 2 and monFilter['gender'] == 'm':
                    return False
            # level
            if "level" in monFilter:
                if(not self.testNumericValue(pokemon.atkIv, monFilter['level'])):
                    return False
            # ivAtk
            if "ivAtk" in monFilter:
                if(not self.testNumericValue(pokemon.atkIv, monFilter['ivAtk'])):
                    return False
            # ivDef
            if "ivDef" in monFilter:
                if(not self.testNumericValue(pokemon.defIv, monFilter['ivDef'])):
                    return False
            # ivSta
            if "ivSta" in monFilter:
                if(not self.testNumericValue(pokemon.staIv, monFilter['ivSta'])):
                    return False
            # cp
            if "cp" in monFilter:
                if(not self.testNumericValue(pokemon.cp, monFilter['cp'])):
                    return False
            
            # all fine
            return True


    # test the found pokemon value against the filter condition 
    def testNumericValue(self, foundValue, filterCondition):
        splitted = filterCondition.split(':')
        condFilter = splitted[0]
        valFilter = int(splitted[1])
        if(condFilter == "=="):
            return foundValue == valFilter
        if(condFilter == ">="):
            return foundValue >= valFilter
        if(condFilter == "<="):
            return foundValue <= valFilter
        if(condFilter == "!="):
            return foundValue != valFilter
    

    def testConfig(self):
        for monFilter in self.filterConfig['mons']:

            # first check if the mon id is set
            helper.hasOwnProperty(monFilter, 'monId', self.filterType)
            
            # tmp filter name for improved error finding
            tmpFilterName = self.filterType +" mon-id- "+str(monFilter['monId'])
            
            # if property is set check for errors
            if('ivAtk' in monFilter):
                # first check for the numeric property if the condition and value is set
                helper.checkIfConditionAndValueIsSet(monFilter['ivAtk'], tmpFilterName)
                # then split
                splittedAtk =  monFilter['ivAtk'].split(':')
                # get the condition
                condFilterAtk = splittedAtk[0]
                # check if the condition is valid
                helper.checkAdvancedMonFilterCondition(condFilterAtk, tmpFilterName)
                # now get the value
                valueFilterAtk = int(splittedAtk[1])
                # and test if the value is valid (stats must be in range 0-15)
                helper.checkIfValueIsInRange(valueFilterAtk, 0, 15, "ivAtk", tmpFilterName)

            if('ivDef' in monFilter):
                # first check for the numeric property if the condition and value is set
                helper.checkIfConditionAndValueIsSet(monFilter['ivDef'], tmpFilterName)
                # then split
                splittedDef =  monFilter['ivDef'].split(':')
                # get the condition
                condFilterDef = splittedDef[0]
                # check if the condition is valid
                helper.checkAdvancedMonFilterCondition(condFilterDef, tmpFilterName)
                # now get the value
                valueFilterDef = int(splittedDef[1])
                # and test if the value is valid (stats must be in range 0-15)                
                helper.checkIfValueIsInRange(valueFilterDef, 0, 15, "ivDef", tmpFilterName)

            if('ivSta' in monFilter):
                # first check for the numeric property if the condition and value is set                                         
                helper.checkIfConditionAndValueIsSet(monFilter['ivSta'], tmpFilterName)
                # then split
                splittedSta =  monFilter['ivSta'].split(':')
                # get the condition
                condFilterSta = splittedSta[0]     
                # check if the condition is valid
                helper.checkAdvancedMonFilterCondition(condFilterSta, tmpFilterName)
                # now get the value                
                valueFilterSta = int(splittedSta[1])
                # and test if the value is valid (stats must be in range 0-15)   
                helper.checkIfValueIsInRange(valueFilterSta, 0, 15, "ivSta", tmpFilterName)

            if('cp' in monFilter):
                # first check for the numeric property if the condition and value is set                                         
                helper.checkIfConditionAndValueIsSet(monFilter['cp'],    tmpFilterName)
                # then split
                splittedCp =   monFilter['cp'].split(':')
                # get the condition
                condFilterCp =  splittedCp[0]
                # check if the condition is valid
                helper.checkAdvancedMonFilterCondition(condFilterCp , tmpFilterName)

            if('level' in monFilter):
                # first check for the numeric property if the condition and value is set
                helper.checkIfConditionAndValueIsSet(monFilter['level'], tmpFilterName)
                # then split
                splittedLevel =   monFilter['level'].split(':')
                # get the condition
                condFilterLevel =  splittedLevel[0]
                # check if the condition is valid
                helper.checkAdvancedMonFilterCondition(condFilterLevel , tmpFilterName)

            if('gender' in monFilter):
                helper.checkGenderValue(monFilter['gender'], tmpFilterName)

        self.logger.info("Filter config for "+ self.filterType +" is fine.")
