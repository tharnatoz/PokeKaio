#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class MessageParser():

    def __init__(self, locale, messenger):
        self.locale = locale
        self.messenger = messenger

        # load messages.json - default
        with open('message/lang/{}/messages.json'.format(self.locale)) as f:
            self.messages = json.load(f)
    
    # replace the placeholder with the infos  
    def replace(self, string, infDict):
        if string is None:
            return None
        s = string.encode('UTF-8')
        for key in infDict:
            s = s.replace("{"+key+"}", str(infDict[key]))
        return s
    
    # returns the message utf-8 encoded
    def getMessage(self, key):
        s = self.messages[self.messenger][key]
        string = s.encode('UTF-8')
        return string