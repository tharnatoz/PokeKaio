#!/usr/bin/env python
# -*- coding: utf-8 -*-

from notification.telegram import telegram

class NotificationManager:

    def __init__(self, config, locale):
        
        self.config = config
        self.messengerType = config['messenger']['type']
        
        # add here you new schema connection 
        if(self.messengerType == 'telegram'):
            self.notificationCnx = telegram.Telegram(config['name'],config['messenger'], locale)
            pass

        if(self.notificationCnx is None):
            raise ValueError('Unknown messenger type' + self.notificationCnx + '. Please check your channels.json')

    def getMessenger(self):
        return self.notificationCnx