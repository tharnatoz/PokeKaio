#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty
import logging

from db_wrapper import connector

# https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python

class BaseWrapper:
    __metaclass__ = ABCMeta

    def __init__(self, config):

        # get logger instance
        logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # set config
        self.config = config

        # get databse connector
        self.databaseConnector = connector.DatabaseConnector(config)

        super(BaseWrapper, self).__init__()

  

    @abstractmethod
    def getPokemonData(self, raw=False):
        pass    

    @abstractmethod
    def getRaidData(self, raw=False):
        pass 

    @abstractmethod
    def getQuestData(self,raw=False):
        pass 
    
    @abstractmethod
    def parsePokemonDataToModel(self, rawData):
        pass

    @abstractmethod
    def parseRaidDataToModel(self, rawData):    
        pass 

    @abstractmethod
    def parseQuestDataToModel(self, rawData):
        pass 
