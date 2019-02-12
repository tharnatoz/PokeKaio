# PokeKaio
### Welcome to PokeKaio - your Kaioshin that supports you to get the very best

### What is PokeKaio
PokeKaio is a RocketMap extensions that checks the database for Pokemon and sends you a message to a telegram channel.
You will need a scanner that collects the Pokemon data and writ it into your RocketMap database, PokeKaio then checks this data and sends you a message if a desired one is found.


### Requirements
* Python 2.7
* A [RocketMap](https://github.com/RocketMap/RocketMap) Database 
* A Working Scanner to collect the data and writes it into you RM database


### How to run

- git clone ```https://github.com/RocketMap/RocketMap.git```
- ```pip install -r requirements.txt ```
- ```cp config/config.ini.example config/config.ini```
- ```cp config/channels.json.example config/channels.ini```
- add your config in config.ini and channels.json (example configs are in .example files)


##### Geofence
visit [http://geo.jasparke.net/](http://geo.jasparke.net/)

add at the end of each line a  ; 


##### Telegram Support

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
   "messenger": "telegram",
   "channelId": "<your_channel_id_goes_here>",
   "botToken": "<your_bot_toke_goes_here>",
   "geofence": "",
   "geofence_exclude": "",
   "filter": {
    "type": "iv",
    "whitelist": [],
    "blacklist": [],
    "ivMax": "",
    "ivMin": ""
   }

```
##### Filter
Currently PokeKaio supports 2 Types of filter. IV and a Whitlist filter for a Super Rare Channel for e.g.

**Whitelist**

* add your Pokemon Id to the whitlist: [1,2,147,201]

``` 
  "filter": {
    "type": "whitelist",
    "whitelist": [147,201,214,317],
    "blacklist": [66,100],
    "ivMax": "",
    "ivMin": ""
   }
```   
  

**IV** 
* set you min and max IV if you only want a specific IV then set for e.g. ```"minIv": "45"``` and ```"maxIv": "45"``` for a 100IV Channel
```  
  "filter": {
    "type": "iv",
    "whitelist": [],
    "blacklist": [66,100],
    "ivMax": "45",
    "ivMin": "44"
   }
```
**Blacklist** The Blacklist is for every filter, each Pokemon Id in the list will be Ignored


