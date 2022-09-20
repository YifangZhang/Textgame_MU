'''
This is a remake game for 奇迹MU Flash game.
It will be included in 3 areas:
1. top area will be visual area, showing stats, equip, pots, gems, and gold
-- 1.1 character status
-- 1.2 character equipments
-- 1.3 pots & gems & gold

2. the middle area will be action area, players can click buttons to get action going
3. the botton area will be save/load area:
-- if you have no character, you will need to hit "load" or "new" button
-- if you already have a character created, you can hit "save" button
'''
import tkinter as tk

class Player:

    def __init__(self, command_type, class_type, player_name):
        if (command_type == "create"):
            if(class_type == "warrior"):
                self.job = "warrior"
                self.name = player_name
                self.level = 1
                self.APLeft = 0
                self.luck = 0
                self.int = 15
                self.vit = 18
                self.dex = 18
                self.str = 30
                self.attack = round(self.str*0.5) ## TODO: will need to add equip atk
                self.defense = round(self.dex*1) ## TODO: will need to add equip def
                self.HP = round(self.vit*2+self.level*2+80)
                ## self location ##
                self.location = "land of brave"
                self.monster = "goblin"
                ## self equips ##
                self.lefthand = ["none", 0, 0, 0]
                self.righthand = ["none", 0, 0, 0]
                self.head = ["none", 0, 0, 0]
                self.body = ["none", 0, 0, 0]
                self.leg = ["none", 0, 0, 0]
                self.arm = ["none", 0, 0, 0]
                self.foot = ["none", 0, 0, 0]
            else:
                return None
        else:
            return None


root = tk.Tk()

## loading a new warrior player
player = Player(command_type="create", class_type="warrior", player_name="wind")

## 1.1 adding the character status:
## adding attack, defense, HP
tk.Label(root, text="Character Stats |", font="-weight bold").grid(row=0, column=0)
L_attack = tk.Label(root, text=("Attack: " + str(player.attack)))
L_attack.grid(row=1, column=0)
L_defense = tk.Label(root, text=("Defense: " + str(player.defense)))
L_defense.grid(row=2, column=0)
## adding location, monster
tk.Label(root, text="Map Information", font="-weight bold").grid(row=4, column=0)
L_location = tk.Label(root, text=("Location: " + player.location))
L_location.grid(row=5, column=0)
L_monster = tk.Label(root, text=("Monster: " + player.monster))
L_monster.grid(row=6, column=0)
## adding AP_Left, luck, int, vit, dex, str
tk.Label(root, text="Character Attributes", font="-weight bold").grid(row=0, column=1)
L_APleft = tk.Label(root, text=("AP Left: " + str(player.APLeft)))
L_APleft.grid(row=1, column=1)
L_luck = tk.Label(root, text=("Luck: " + str(player.luck)))
L_luck.grid(row=2, column=1)
L_int = tk.Label(root, text=("Intelligent: " + str(player.int)))
L_int.grid(row=3, column=1)
L_vit = tk.Label(root, text=("Vitality: " + str(player.vit)))
L_vit.grid(row=4, column=1)
L_dex = tk.Label(root, text=("Dexterity: " + str(player.dex)))
L_dex.grid(row=5, column=1)
L_str = tk.Label(root, text=("Strength: " + str(player.str)))
L_str.grid(row=6, column=1)
L_HP = tk.Label(root, text=("HP: " + str(player.HP)))
L_HP.grid(row=7, column=1)

## 1.2 adding character equipments:
tk.Label(root, text="Character Equipment", font="-weight bold").grid(row=8, column=0)
L_lefthand = tk.Label(root, text=("left hand: " + str(player.lefthand[0])))
L_lefthand.grid(row=9, column=0)
L_righthand = tk.Label(root, text=("right hand: " + str(player.righthand[0])))
L_righthand.grid(row=10, column=0)
L_head = tk.Label(root, text=("helmet: " + str(player.head[0])))
L_head.grid(row=11, column=0)
L_body = tk.Label(root, text=("chest armor: " + str(player.body[0])))
L_body.grid(row=12, column=0)
L_leg = tk.Label(root, text=("trousers: " + str(player.leg[0])))
L_leg.grid(row=13, column=0)
L_arm = tk.Label(root, text=("shoulder: " + str(player.arm[0])))
L_arm.grid(row=14, column=0)
L_foot = tk.Label(root, text=("shoes: " + str(player.foot[0])))
L_foot.grid(row=15, column=0)

## 1.3 adding gems (5 total), pots, gold (gold can be places in column=0)

root.mainloop()