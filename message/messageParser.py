#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class MessageParser():

    def __init__(self, locale):
        self.locale = locale

        # load messages.json - default
        with open('message/lang/{}/messages.json'.format(self.locale)) as f:
            self.messages = json.load(f)
        

    def getPokemonInfo(self, mKind, monName, monGender):
        string =  self.messages[mKind]['pokemon_info']
        #s = string.encode('utf-8')
        return  string.format(mon_name = monName, mon_gender=monGender, ts="ds")