#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class MessageParser():

    def __init__(self, locale):
        self.locale = locale

        # load messages.json - default
        with open('message/lang/{}/messages.json'.format(self.locale)) as f:
            self.messages = json.load(f)
        

    def getPokemonInfo(self, monName, monGender):
        return u''+self.messages['pokemon_info'].format(monName, 1)
