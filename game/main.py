'''
Due to the title of the game, I will try to recreate the Flash Browser game of MU into Python text-based format:
1. warrior: 27 str, 20 dex, 20 vit, 15 int
2. mage: 18 str, 18 dex, 15 vit, 30 int
3. archer: 22 str, 25 dex, 20 vit, 15 int
4. calculated hp 60+level*2+vit*2 warrior 
   60+level*1+vit*1 mage, 60+level*2+vit*1
5. notes:
1、智力：法师+1攻击力
2、体力：法师+1生命，战士+2生命，弓箭手+1生命
3、敏捷：法师+0.75防，战士+1防，弓箭手+1防
4、力量：战士+0.5攻，弓箭手+0.75攻
5、升级：法师+1血，弓箭手+2血，战士+3血
'''

player = {
    "name": "Player",
    "class": "warrior",
    "level": 1,
    "exp": 0,
    "gold": 10000,
    "skills": {},
    "location": "forest",
    "monster": "goblin",
    "gems":
    {   
        "life_gem": 0,
        "blessing_gem": 0,
        "spirit_gem": 0,
        "maya_gem": 0,
        "feather_gem": 0,
        "hp_pot": 100
    },
    "equipments":
    {
        "head": {"name": "empty", "stats":[0,0,0]},
        "chest": {"name": "empty", "stats":[0,0,0]},
        "main": {"name": "empty", "stats":[0,0,0]},
        "off": {"name": "empty", "stats":[0,0,0]},
        "pants": {"name": "empty", "stats":[0,0,0]},
        "shoes": {"name": "empty", "stats":[0,0,0]},
        "gloves": {"name": "empty", "stats":[0,0,0]},
        "wings": {"name": "empty", "stats":[0,0,0]}
    },
    "str": 27,
    "dex": 20,
    "vit": 20,
    "int": 15,
    "cur_hp": 102
}

### step 1: player name, player class, or load ###

## TODO: game intro text

## TODO: save and load system

### step 2: player entered the main screen:
## TODO: basic player info
'''
1. name, class, level
2. current exp, needed exp (lvl^3+lvl*10+100), gold
3. atk, def, cur_hp/total_hp, special skills
4. location, monster name
5. all those freaking gems: life, blessing, spirit, maya, feather, hppot
6. all equipments: head, chest, main, off, pants, gloves, shoes, wings
'''

## TODO: basic combat option
'''
1. monster exp: math.floor((monster level)^2/10 + 10)
2. making sure both sides finished damage step, then check which wins
3. creating the combat option on text
4. monster drop, should use the random number generator to consider the drop
    in theory, one monster should only drop 1 tier of items depending on their level
5. 
'''

## TODO: basic stats boosting system
'''
1. adding stats will affect the atk, def, and hp
2. skills implementation?
'''

## TODO: modification system for enchance the weapon stats
'''
1. enchancing the weapon after weapon dropped
2. go +10 & +11 weapon
3. go maya weapon
4. go wings
'''

## TODO: basic shopping
'''
1. buying gems
2. buying pots
'''

## TODO: choose monster and change location
'''
1. monster+location list in json
2. going to work on demodel all monsters
'''



