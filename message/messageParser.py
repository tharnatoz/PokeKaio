#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class MessageParser():

    def __init__(self, locale):
        self.locale = locale

        # load messages.json - default
        with open('message/lang/{}/messages.json'.format(self.locale)) as f:
            self.messages = json.load(f)
        
    def replace(self, string, infDict):
        if string is None:
            return None
        s = string.encode('UTF-8')
        for key in infDict:
            s = s.replace("{"+key+"}", str(infDict[key]))
        return s