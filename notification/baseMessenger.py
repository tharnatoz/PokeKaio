#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty
import logging
from requests import get

from message import messageParser

# https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python

class BaseMessenger:
    __metaclass__ = ABCMeta

    def __init__(self, config):

        # get logger instance
        logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(threadName)s  %(name)s -- %(message)s',level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # set config
        self.config = config

        # get message parser
        self.message = messageParser.MessageParser('de')

        # request module
        self.getRequest = get

        super(BaseMessenger, self).__init__()

  

    '''
	=====================================
	| Full Message Methods
	=====================================
	|
	| Function that are used for sending notification 
    |
    | Inherit this class for your own messanges service
    | and implement your logic
    |
	|
	'''
    @abstractmethod
    def sendPokemonNotification(self):
        pass
    
    @abstractmethod
    def sendRaidNotification(self):
        pass

    @abstractmethod
    def sendQuestNotification(self):
        pass 

    @abstractmethod
    def checkForErrors(self):
        pass