#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty
import logging

# https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python

class BaseFilter:
    __metaclass__ = ABCMeta

    def __init__(self, filterConfig, filterType):
        self.filterConfig = filterConfig
        
        self.filterType = filterType

        # data Type is require e.g. Pokemon, Quest, Raid ...
        if ('dataType' in self.filterConfig):
            self.dataType = self.filterConfig['dataType']
        else:
            raise ValueError("Missing Field: 'DataType' in Filter. Please check your channels.json. Error raised in Filter with type:", self.filterType )

        # name is required
        if ('name' in self.filterConfig):
            self.name = self.filterConfig['name']
        else:
            raise ValueError("Missing Field: 'name' in Filter. Please check your channels.json. Error raised in Filter with type:", self.filterType )
        
        # get logger instance
        logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # custom filter check
        self.testConfig()

        super(BaseFilter, self).__init__()

    '''
    Override this method with your own test logic e.g. whitelist 

    if(pokemon.pokemonId in whitelist):
        return True
    else:
        return False

    @return param bool
    '''
    @abstractmethod
    def isSatisfied(self, pokemon):
        pass
    
    '''
    Filter test method, please override this method with your tests if all fields that are required are set,
    if something is missing you must rais a ValueError.

    e.g. a whitelist filter need a white list with at least one Pokemon id in it. If this field is not set 
    raise an ValueError.
    '''
    @abstractmethod
    def testConfig(self):
        pass    
