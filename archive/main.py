
'''
## this first tkinter game I will be making will be totally copy of the game
## qiji MU the flash game. I think it is an interesting game and wanted to copy
## it into the python tkinter version.
## we can fix some op stats and stuff, but it will go into 2 steps
## first step we will be completely mimic the game progress

Tkinter version author: Yifang Zhang

The original game involves the following game functionalities:

1. main interface:
    -- display the stats of items
    -- display player's stats
    -- display the loot
    -- restart & exit buttons
    -- gems + pots
    -- select map & mobs
    -- add player's stats
    -- create a new character
    -- helping window
    -- save button
    -- combat indicator for 1 or 2
    -- use different gems
    -- combine gems for higher level of weapons
    -- gold indicator
    
2. select mobs & select place interface:
    -- enter different places
    -- select different mobs
    -- display the mobs' stats


'''

import tkinter
import random
import pprint

## define the player variable ##
my_player = {
    'name' : 'wind',
    'class' : 'warrior',
    'stats' : {'str':28, 'dex':20, 'vit':25, 'int':10},
    'equip' : {'left':None, 'right':None, 'head':None, 'body':None,
               'pants':None, 'shoes':None, 'gloves':None, 'wings': None},
    'location' : 'beginner_village',
    'current_HP' : 110+25*2+1*2, ## 110+vit*2+lv*2 ##
    'skills' : [],
    'monster' : 'goblin',
    'level' : 1,
    'exp' : 0,
    'items': []
    }

short_sword = {
    'name' : 'short sword',
    ''
    }

## define all the helper functions for my_player ##
def find_my_raw_combat_stats(p):
    if(p['class'] == 'warrior'):
        attack = p['stats']['str']*0.5
        defense = p['stats']['dex']*1.0
        hp = p['stats']['vit']*2 + p['level']*2 + 110
        return [attack, defense, hp]
    if(p['class'] == 'archer'):
        attack = p['stats']['str']*0.75
        defense = p['stats']['dex']*1.0
        hp = p['stats']['vit']*1 + p['level']*2 + 80
        return [attack, defense, hp]
    if(p['class'] == 'mage'):
        attack = p['stats']['int']*1.0
        defense = p['stats']['dex']*0.75
        hp = p['stats']['vit']*1 + p['level']*1 + 60
        return [attack, defense, hp]

def equip_item(p, item):
    



## testing lines here ##
pprint.pprint(my_player)
pprint.pprint(find_my_raw_combat_stats(my_player))





