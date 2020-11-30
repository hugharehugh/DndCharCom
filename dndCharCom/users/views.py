from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
#we need our User login model
from .models import User
from django.contrib.auth import login, logout, authenticate
#using Djangos built in user functionality, so we import from django.

#define how the user signup function will work, taking in the request from
#the application as
def user_signup(request):
    #if the request is a post, meaning putting data
    if request.method=='POST':
        #the f_name value passed in the request will be set to the value on the left
        #of the equation. I am using the same names for form values and DB values
        #for ease of coding.
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        password = request.POST['password']
        email = request.POST['email']
        username = request.POST['username']
        security_question = request.POST['security_question']
        security_answer = request.POST['security_answer']
        
        #once the values are stored in this function, create an actual data object and
        #pass it to the user value in the DB (i think)
        user = User.objects.create_user(first_name=f_name,last_name=l_name,password=password,username=username,email=email,security_question=security_question,security_answer=security_answer)
        #return a redirect to the login page so the page refreshes and loads login
        return redirect('users:login')
    #in case they messed up somehow, just relaod the landing page
    elif request.method == 'GET':
        return render(request, 'users/index.html')

#define the user login function
def user_login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        #only try to login if they provide a login value
        if user is not None:

            login(request,user)

        return redirect('posts:index')
    elif request.method == 'GET':
        return render(request, 'users/login.html')


#logout
def user_logout(request):
    logout(request)
    return redirect('users:login')
