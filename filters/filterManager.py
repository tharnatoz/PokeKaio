#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.pokemon.mon_whitelist import Mon_Whitelist
from filters.pokemon.mon_iv import Mon_Iv
from filters.pokemon.mon_iv_whitelist import Mon_Iv_Whitelist
from filters.pokemon.mon_stats import Mon_Stats

class FilterManager:

    def __init__(self, filterConfig):
        
        self.filterConfig = filterConfig
        self.filter = None

        # add here you new filter type
        if(self.filterConfig['type'] == 'mon_whitelist'):
            self.filter = Mon_Whitelist(self.filterConfig)
        elif(self.filterConfig['type'] == 'mon_iv'):
            self.filter = Mon_Iv(self.filterConfig)
        elif(self.filterConfig['type'] == 'mon_iv_whitelist'):
            self.filter = Mon_Iv_Whitelist(self.filterConfig)
        elif(self.filterConfig['type'] == 'mon_stats'):
            self.filter = Mon_Stats(self.filterConfig)

        if(self.filter is None):
            raise ValueError('Unknown filter type ' + filterConfig['type'] + '. Please check channels.json')

    def getFilter(self):
        return self.filter