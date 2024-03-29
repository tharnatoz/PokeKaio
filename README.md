# PokeKaio
### Welcome to PokeKaio - your Kaioshin that supports you to become the very best

### What is PokeKaio
PokeKaio is a RDM-Map extension that checks the database for Pokemon and sends you a message to a telegram channel.
You will need a scanner that collects the Pokemon data and write it into your RocketMap database, PokeKaio than checks this data and sends you a message if a desired one is found.


### Requirements
* Python 2.7
* RDM-Sytem


### How to run

- git clone ```git@github.com:tharnatoz/PokeKaio.git```
- ```pip install -r requirements.txt ```
- ```cp config/config.ini.example config/config.ini```
- ```cp config/channels.json.example config/channels.ini```
- add your config in config.ini and channels.json (example configs are in .example files)

### Language Settings

in config.ini under ```settings``` set yout locale e.g. ```locale = de```

current support ```en``` and ```de```

### Geofence
visit [http://geo.jasparke.net/](http://geo.jasparke.net/)

add at the end of each line a  ; 

### Reverse Geocoding

copy your [google api](https://developers.google.com/maps/documentation/geocoding/get-api-key) into config.ini
and set ```enable_reverse_geocoding = true```


## Messanger Support

At the moment PokeKaio only supports Telegram notifications

### Telegram

1. Create a Telegram Channel
2. Copy channel link in channel_id
3. Create a bot via [BotFather](https://core.telegram.org/bots#6-botfather)
4. Add your new Bot as **Admin** to your recent created channel
5. Copy yout bot token to channel.json 
 
```
  {
   "name": "TestChannel",
   "type": "pokemon",
   "isActive": "true",
   "geofence": "",
   "geofence_exclude": "",
   "messenger": {
    "type":"telegram",
    "channelId": "<your_channel_id_goes_here>",
    "botToken": "<your_bot_token_goes_here>"
   },
   "filter": {
    "type": "mon_iv",
    "whitelist": [],
    "blacklist": [],
    "ivMax": "",
    "ivMin": ""
   }
```
## Filter

At the moement PokeKaio supports only Pokemon filter.

* mon_whitelist: Whitelist check
* mon_iv: Checks for an IV-Range
* mon_iv_whitelist: Check for an IV-Range with a given Pokemon whitelist
* mon_stats: checks for PVP-Mons values maxAtk, minDef, minSta and maxCP
* mon_advanced_stats: test pokemon stats against the configured filter values


### Filter examples

**Whitelist (mon_whitelist)**

* add your Pokemon Id to the whitlist: [1,2,147,201]

``` 
  "filter": {
    "type": "mon_iv",
    "name": "PokeKaio_mon_whitelist_example",
    "dataType": "pokemon",
    "whitelist": [147,201,214,317],
    "blacklist": [1,54,32]
   }
```   
  

**IV (mon_iv)** 
* set min and max IV if you only want a specific IV then set for e.g. ```"minIv": "45"``` and ```"maxIv": "45"``` for a 100IV Channel
```  
  "filter": {
    "type": "mon_iv",
    "name": "PokeKaio_mon_iv_example",
    "dataType": "pokemon",
    "blacklist": [66,100],
    "ivMax": 45,
    "ivMin": 44
   }
```

**IV-Whitelist (mon_iv_whitelist)** 
* set min and max IV if you only want a specific IV then set for e.g. ```"minIv": "45"``` and ```"maxIv": "45"``` and the Pokemon Id's that shoult report.
```  
  "filter": {
    "type": "mon_iv_whitelist",
    "name": "PokeKaio_mon_iv_whitelist_example",
    "dataType": "pokemon",
    "whitelist": [201,1,149],
    "blacklist": [66,100],
    "ivMax": 45
    "ivMin": 44

   }
```

**Stats (mon_stats)** 
* set  iVmaxAtk, iVminDef, iVminSta and maxCP if you want to, you can set blacklist filter.
```  
  "filter": {
    "type": "mon_stats",
    "name": "PokeKaio_mon_stats_example",
    "dataType": "pokemon",
    "iVmaxAtk": 2,
    "iVminDef": 14,
    "iVminSta": 14,
    "maxCP": 1500
   }
```

**Advanced Pokemon (mon_advanced)**

The filter takes an array of Pokemon with defined key/values you want to check. Add as many you need!


Allowed Properties

* ```ivAtk``` (Attack Stat, must be in range 0-15)
* ```ivDef``` (Defense Stat, must be in range 0-15)
* ```ivSta``` (Stamina Stat, must be in range 0-15)
* ```cp``` (Combat Points)
* ```level``` (The Pokemon level)
* ```gender``` (Pokemon gender, values: m for male, f for female)

If you don't want to test any of these values, don't add it to your filter.

You must always set the Pokemon Id ```monId```


**For numeric properties only (ivAtk, ivDef, ivSta, cp, level)**

The definition must follow the rule: ```{key}: {condition:value} ``` 

e.g. for attack stat greater or equal 14 set ```ivAtk: ">=:14" ```

Allowed conditions are:

* ```==``` equal test
* ```!=``` not equal test
* ```<=``` lower or equal test
* ```>=``` greater or equal test


***Big Thanks to Flo and his PVP-Filter***.

The preconfigured PVP-Filter can you find here: [https://github.com/1522784/Pokeland-PvP-Suche](https://github.com/1522784/Pokeland-PvP-Suche). 
Just configure your channel and copy the array from Search.json into your mon_advanced under ```"mons"```
and its ready to use.

```
"filter": {
 "type": "mon_advanced",
 "dataType": "pokemon",
 "name": "PokeKaio_mon_advanced_stats_example",
 "mons":[{
   "monId": 504,
   "ivAtk" : "<=:15",
   "ivDef" : ">=:12",
   "ivSta" :">=:13",
   "cp": "<=:1500"
  },
  {
   "monId": 3,
   "ivAtk" : "<=:2",
   "ivDef" : ">=:12",
   "cp": "<=:1500",
   "gender": "f",
   "level": "==:35"
  }]
}
```


**Blacklist** The Blacklist is for every filter(except for mon_advanced), each Pokemon Id in the list will be ignored, even if the ids are in the whitelist
