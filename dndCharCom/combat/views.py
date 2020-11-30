from pathlib import PosixPath
from typing import ContextManager
from django.http import request
from django.shortcuts import render, redirect
from .models import Char_Model,Combat
from django.contrib.auth.decorators import login_required

# the index view will display the character creation panel, and a list of existing characters
#by name and image if one is provided
def index(request):
    #the thing below is a description of the function paramaters not a comment
    '''displays all character models, probably definitely needs more to function'''
    characters = Char_Model.all
    context = {
        'characters': characters,
    }

    return render(request,'combat/index.html',context)

#save character model view 
# NEED TO MAKE FORM FOR CHARACTER IN INDEX.HTML
# ALSO THE NAMING OF COMBAT VS CHAR VS WHATEVER IS DUMB! FIX YOUR CODE BRO
#THE FORM WILL PROVIDE THE DATA FOR THE REQUEST.
def save_char(request):

    form = request.Post
    #need stuff like hp, bakground, class, total hp, blah blah blah
    