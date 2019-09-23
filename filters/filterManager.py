#!/usr/bin/env python
# -*- coding: utf-8 -*-

from filters.pokemon.whitelist import Whitelist as mon_whitelist
from filters.pokemon.iv import Iv as mon_iv

class FilterManager:

    def __init__(self, filterConfig):
        self.availableFilterTypes = ["mon_whitelist", 'mon_iv', 'whitelist_iv', 'stats']

        if filterConfig['type'] not in self.availableFilterTypes:
            raise ValueError('Unknown filter type ' + filterConfig['type'] + '. Please check channels.json')

        self.filterConfig = filterConfig

        if(self.filterConfig['type'] == 'mon_whitelist'):
            self.filter = mon_whitelist(self.filterConfig)
        elif(self.filterConfig['type'] == 'mon_iv'):
            self.filter = mon_iv(self.filterConfig)

    def getFilter(self):
        return self.filter