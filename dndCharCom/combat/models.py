from os import O_TRUNC
import random
from random import randint
from django.db import models
from dndusers.models import DnDUser
from django.db.models.enums import IntegerChoices
from django.db.models.fields import DecimalField, IntegerField
# Create your models here.
from django.db import models

class MyModel(models.Model):
    my_image = models.ImageField(upload_to='images/')
#dndCharCom is meant to recreate tabletop RPG combat including random dice rolls by click.

#Character model will have normal range of stats

class Combat(models.Model):
    #need to pull in two character models
    #save processing power by rolling first, and dont bother figuring out damage if they miss
    #so check roll + roll modifiers against AC
            # if I want to keep coding this I'll need to address a gap in the future which is:
            # in DnD you can hit on a miss sometimes. Wacky spells / manuevers can change the
            # outcome of a roll before the consequences of the roll are made final
            # divination wizards! (shakes fist at cloud)
    damage = 0
    # put their stats into the combat equations, apply damage modifiers, remove the amount
    # of damage done from the characters health.
    # then do the same thing with the other character.

    #question for MVP?! do I want to take in a roll / click from the "player"?
    # would be kinda cool to let them click a button on the screen and see their "roll"
    # which would be produced by a random number function    
    def __str__(self):
        return self.damage


class Char_Model(models.Model):
    #the statmaker randomly rolls 4 sets of d6 and returns the results
    def statmaker():
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll3 = random.randint(1,6)
        statlist = ['str_stat','con_stat','wis_stat','char_stat','int_stat','dex_stat']
        stats = 0
        for stats in statlist:
            stats = roll1 + roll2 + roll3
        return stats
    # character models is the part of the app that lets users create and save characters
    # the character model maker will allow the user to make any functional model I have
    # finished coding.
    # the MVP is fighter character models, so that is what I am coding first
    name = models.CharField(max_length=24,blank=False)
    background = models.CharField(max_length=200,blank=False)
    available_actions = models.IntegerField(default=1,blank=True)
    char_image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(DnDUser,on_delete=models.CASCADE)
    hp = models.IntegerField() ####### FIX THIS
    wpn_dmg_dice = [
            ('club','4'),
            ('dagger','4'),
            ('Greatclub','8'),
            ('Handaxe','6'),
            ('Javelin','6'),
            ('Light Hammer','4'),
            ('Mace','6'),
            ('Quarterstaff','6'),
            ('Sickle','6'),
            ('Spear','6'),
            ('GreatAxe','12')
    ]
    weapon_choice = models.CharField(max_length=12,choices=wpn_dmg_dice,default='Handaxe',blank=False)
    selected_race = models.CharField(max_length=15)
    selected_class = models.CharField(max_length=25)
    size = [
        ('Sml','small'),
        ('Med','medium'),
        ('Lrg','large'),
        ('Gnt','giant'),
        ('BHM','behemoth')
     ] #important for combat rules
    selected_size = models.CharField(max_length=3,choices=size)
    mvmt_speed = models.IntegerField(blank=False)
    armor_type = [
        ('Light','light'), 
        ('Med','medium'),
        ('Hev','heavy'),
        ]
    selected_armor = models.CharField(max_length=12,choices=armor_type,blank=True)
    armor_penalty = models.CharField(max_length=12,blank=True)
    str_stat = models.IntegerField(default=statmaker, blank=False)
    con_stat = models.IntegerField(default=statmaker, blank=False)
    int_stat = models.IntegerField(default=statmaker, blank=False)
    wis_stat = models.IntegerField(default=statmaker, blank=False)
    char_stat = models.IntegerField(default=statmaker,blank=False)
    dex_stat = models.IntegerField(default=statmaker, blank=False)
    armor_Class = models.IntegerField(default=statmaker, blank=True)
    #need to figure out what to multipy dice by.
    #a d4 is literally 1 thru 4 all equally likely, but weapon damage is fixed. so a javeline
    #always does d6 damage + other stuff
    #should I just have a weapons list?
    #to make this work at first I could let the user set it, then later on build the weapon library
    #and have the user pick from the dropdown of weapons, then apply the correct damage
    modifiers = models.IntegerField(default=1,blank=True)
    spell_slots = models.IntegerField(default=0,blank=True)
    
    #don't forget to actually make the model function
    def __str__(self):
        return self.name 

#weapons need to be chosen during character creation, no switching weopons 
# until character customization is figured out
    class Weapons(models.Model):
        melee_weapons = {
            'club':[4,'b'],
            'dagger':[4,'p'],
            'Greatclub':[8,'b'],
            'Handaxe':[6,'s'],
            'Javelin': [6, 'p'],
            'Light Hammer': [4, 'b'],
            'Mace': [6, 'b'],
            'Quarterstaff': [6,'b'],
            'Sickle': [6, 's'],
            'Spear': [6, 'p'],

        }

        ranged_weapons = {
            'Crossbow': [8, 'p'],
            'Dart': [4,'p'],
            'Shortbow': [6,'p'],
            'Sling': [4,'b'],
        }

    #charModel:
#     hp: integer (represent hit points)
#     name: string
#     available_actions: integer (most characters have one action and one bonus action per turn plus a free action)
#     wpn_dmg_dice: d2,d3,d4,d6,d8,d10,d12
#     modifiers: integer that interacts with wpn_dmg_dice
#     spell_slots: 1st:0,2nd:0,3rd:0,4th:0,5th:0,6th:0,7th:0,8th:0,9th:0 
#     # spell slots are used to cast spells, no slots, no spells
#     special_actions: integer (some classes like fighter allow the use of additional dice, would use that here)
#     race: from char creation
#     # height: for flavor?
#     size: (small, medium, large, giant, behemoth?) important for combat rules
#     mvmt_speed: (advanced goal is to figure out combat arena and movement)
#     armor_type: light, medium, heavy
#     armor_penalty: non_casting for casters in heavy plate for example
#     str_stat: int
#     # con_stat: int
#     int_stat: int
#     wis_stat: int
#     char_stat: int
#     dex_stat: int
#     armor_Class: int
#     status: this will be important for spell / fighting due to prone condition and fighter combat manuevers

#     #stats will be set at character creation and stored in the character model

#     #for combat the two character models will "attack" each other by rolling a d20
    
#     #12 on the Die 

#     #combat equation
#     attack_roll = d20_roll + str/dex mod + (offhand modifier if relevant)
#     #damage will be applied to the models on a hit 
#     if attack_roll is higher than armor_Class then apply attack damage:

#     attack = str/dex mod + wpn_dmg_dice(modifiers go here)
    
#     charModel_fighter loses attack amount of hp

#     NEED TO FLESH OUT:

#     action rules: since some characters can forego actions, take secondary actions, can have additional actions granted to them
    
#     armor_class rules: can simply ignore and only go on AC set dsuring character creation, but there are goofy rules that alter combat
    
#     spellcasting rules: depending on what type of spellcaster the character is they get a different number of spell slots and can use them separately. 
#     those should go in the spellcaster classes as much as possible but some rules apply to all spellcaster generally
#     spellcasting_equation = d20_roll + caster_class_mod + modifiers (spellcasting equation only used for "roll to hit spells")

#  spellcasting_equation = d20_roll + caster_class_mod + modifiers (spellcasting equation only used for "roll to hit spells")

#     #class_models:

#     paladin {
#         #spellslots like cleric, similar spell selection list
#         #need domains
#         #smite equation should go here, only allow smiting from within the class #(remember they get to pick whether to smite after the die is rolled but not before the hit is known .... right? double check)
#         #requires spell focus
#     }

#     cleric {
#         #unique class feature all spells immediately available, just gotta pick them each combat #in game its one prayer session per day I think
#         #requires spell focus
#     }    

#     class fighter {
#         #fighter pretty much just whack stuff until they get combat manuevers and secondary actions
#         #secondary action rules go here
#         #combat manuevers
#         #dual wielding?
#         #offhand rules?
#     }

#     class barbarian {
#         rage rules
#         reckless attack rules need to go here, using it gives opportunity on all attacks against you for the round
#         #dual handing rules? is that a class specific thing?
#         #dex vs str thing dont forget #barbarians can pick str or dex as their weapon stat, so there are dex barbarian builds. I think this is not a unique class feature. pretty sure fighters have this to.
#     }

#     class wizard{
#         #spell stuff is a stretch goal, there are so many effects spells can have, and a lot depend on area being a thing
#         #meaning I need a battlegroung and spacing to really show spells correctly
#         #thankfully most of the combat casters just use their spell slots as extra damage on hits
#     }

#     class sorcerer {
#         spell_slots = 2
#         #gotta be honest, I know like nothing about sorcs
#         #gotta learn the rules
#     }

#     rogue{
#         #sneak attack rules
#         #hidden status can be a modifier
#         #technically a hidden character has a 50/50 shot of being hit even on a successful attack roll, so that will complicate things
#         #an observed character can't hide, and this is single combat at least to start
#         #hiding rules are a stretch goal! lol 
#     }
