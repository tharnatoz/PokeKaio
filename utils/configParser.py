#!/usr/bin/env python
# coding: utf8

from ConfigParser import SafeConfigParser

def readConfig():
	parser = SafeConfigParser()
	parser.read('config/config.ini')

	return parser

def configToDict(conf):
	options = {}
	for each_section in conf.sections():
		options[each_section] = {}
		for (each_key, each_val) in conf.items(each_section):
			options[each_section][each_key] = each_val

	return options