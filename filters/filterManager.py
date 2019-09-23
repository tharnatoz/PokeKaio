#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.pokemon.mon_whitelist import Mon_Whitelist
from filters.pokemon.mon_iv import Mon_Iv
from filters.pokemon.mon_iv_whitelist import Mon_Iv_Whitelist

class FilterManager:

    def __init__(self, filterConfig):
        self.availableFilterTypes = ["mon_whitelist", 'mon_iv', 'mon_whitelist_iv', 'mon_stats']

        self.filterConfig = filterConfig
        self.filter = None

        if(self.filterConfig['type'] == 'mon_whitelist'):
            self.filter = Mon_Whitelist(self.filterConfig)
        elif(self.filterConfig['type'] == 'mon_iv'):
            self.filter = Mon_Iv(self.filterConfig)
        elif(self.filterConfig['type'] == 'mon_iv_whitelist'):
            self.filter = Mon_Iv_Whitelist(self.filterConfig)
        elif(self.filterConfig['type'] == 'mon_iv_whitelist'):
            self.filter = None
            #self.filter = Mon_Iv(self.filterConfig)

        if(self.filter is None):
            raise ValueError('Unknown filter type ' + filterConfig['type'] + '. Please check channels.json')

    def getFilter(self):
        return self.filter