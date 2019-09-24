#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db_wrapper.rdm_wrapper import rdm_wrapper as rdm_w

class DbManager:

    def __init__(self, config):
        
        self.schema = config['db_schema']
        self.config = config
        self.databseConnector = None

        # add here you new schema connection 
        if(self.schema== 'rdm'):
            self.databseConnector = rdm_w.RdmWrapper(config)
        
        if(self.databseConnector is None):
            raise ValueError('Unknown database schema ' + schema + '. Please check your config.ini')

    def getDbBridge(self):
        return self.databseConnector