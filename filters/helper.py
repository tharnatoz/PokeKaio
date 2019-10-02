#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
================================

All helper function for filters

================================
'''


'''
================================

Config test funcions

================================
'''


def testWhiteList(filterConfig):
    # test if a whitelist is set
        if('whitelist' not in filterConfig):
            raise ValueError("Missing Field 'whitelist' in Filter with name: "+ filterConfig['name'] +". Please add a whitelist attribute to your filter e.g. 'whitelist': [1,2,32] ")
        
        whitList = filterConfig['whitelist']
        
        # test if the whitelist has at least one pokemon
        if(len(whitList) == 0):
            raise ValueError("Whitelist in Filter with name: "+ filterConfig['name']  +". Please add a whitelist at least one Pokemon Id to your list e.g. 'whitelist': [1,2,32] ")

def testBlackList(filterConfig):
    if('blacklist' not in filterConfig):
        raise ValueError("Missing attribute 'blacklist' in Filter with name: "+ filterConfig['name'] +". Please add a blacklist attribute to your filter e.g. 'blacklist': [] for an empty list ")

def hasOwnProperty(filterConfig, key, fName=""):   
        
	if('name' not in filterConfig):
		filterName = fName
	else:
		filterName = filterConfig['name'] 
        
	if(key not in filterConfig):
		raise ValueError("Missing attribute "+key+" in filter with name: "+ filterName +". Please add this attribute.")

# test if the value is numeric if its provided as string
def isStringDigit(filterConfig, key):
    # cast to string
    val = str(filterConfig[key])
    # val is digit?
    if(not val.isdigit()):
        raise ValueError(key +" in Filter with name "+ filterConfig['name'] +" must be numeric.")

def checkIfValueIsInRange(value, lower, upper, attributeName, filterName):
    if(value > upper or value < lower):
        raise ValueError(attributeName + " is not in range in filter with name: "+filterName+". Allowed values " + str(lower) +"-"+str(upper))

def minMaxIvRangeCorrect(lower, upper, filterName):
    if(lower > upper):
        raise ValueError("The minIv is greater than the maxIv in filter with name: "+ filterName)

def checkAdvancedMonFilterCondition(condition, filterName):
	if(condition != "==" and condition != ">=" and condition != "<="):
		raise ValueError("Unknown advanced filter condition "+str(condition)+" in: "+ filterName)

def checkIfConditionAndValueIsSet(condValue, filterName):
	splitted = condValue.split(':')
	if len(splitted) != 2:
		raise ValueError("There is somthing wrong with your stat/cp definition: "+ filterName + " you must set stat/cp : 'condition:value' ")
