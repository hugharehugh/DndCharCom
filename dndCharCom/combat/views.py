from pathlib import PosixPath
from typing import ContextManager
from django.http import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse
from .models import Char_Model,Combat,MyModel
from django.contrib.auth.decorators import login_required
from dndusers.models import DnDUser
import random

# the index view will display the character creation panel, and a list of existing characters
#by name and image if one is provided

def upload_image(request):
    my_image = request.FILES['my_image']
    model = MyModel(...,my_image=my_image)
    model.save

def index(request):
    #the thing below is a description of the function paramaters not a comment
    '''displays all character models, probably definitely needs more to function'''
    characters = Char_Model.objects.all
    context = {
        'characters': characters,
    }

    return render(request,'combat\index.html',context)

def characters(request):
    characters = Char_Model.objects.all
    context ={
        'characters':characters
    }
    return render(request,'combat\characters.html',context)

#save character model view 
# NEED TO MAKE FORM FOR CHARACTER IN INDEX.HTML
# ALSO THE NAMING OF COMBAT VS CHAR VS WHATEVER IS DUMB! FIX YOUR CODE BRO
#THE FORM WILL PROVIDE THE DATA FOR THE REQUEST.
def save_char(request):

    form = request.POST
    char_model = Char_Model(name=form['name'],background=form['background'],author=request.user,hp=form['hp'],selected_race=form['selected_race'],selected_class=form['selected_class'],weapon_choice=form['weapon_choice'],selected_size=form['size'],mvmt_speed=form['mvmt_speed'],selected_armor=form['selected_armor'],str_stat=form['str_stat'],con_stat=form['con_stat'],int_stat=form['int_stat'],wis_stat=form['wis_stat'],char_stat=form['char_stat'],dex_stat=form['dex_stat'],armor_class=form['armor_class'],char_image=form['upload_image'])
    char_model.save

    return HttpResponseRedirect(reverse('combat:characters'))
    #need stuff like hp, bakground, class, total hp, blah blah blah

def delete(request,char_id):
    char_model = Char_Model.objects.get(pk=char_id)
    char_model.delete()
    return HttpResponseRedirect(reverse('combat:index'))