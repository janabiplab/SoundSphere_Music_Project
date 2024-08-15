from django.shortcuts import render
from .models import Song
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from music.models import models
from django.contrib.auth import logout as auth_logout

@login_required
# Create your views here.
def index(request):
    song=Song.objects.all()
    singer_arr=[]
    for item in song:
        singer_arr.append(item.singer)
    singer_arr.sort()
    new_singer_arr=[]
    for element in singer_arr:
        if len(new_singer_arr)==0:
            new_singer_arr.append(element)
        if new_singer_arr[-1]!=element:
            new_singer_arr.append(element)       
    return render(request,'music/index.html',{'Song':song,"user":request.user,"Singers":new_singer_arr})
     
def SignUp(request):
    
    # user submission form 
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.filter(username=username)
        # if the user name is already exist then show thw message
        if user.exists():
            messages.info(request,"User Name is already exit")    
            return redirect('/SoundSphere/signup/')
         # create the user
        user=User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username

        ) 

        # set the user password
        user.set_password(password)

        # save the user
        user.save()

        # display a message for successful registration
        messages.info(request,"Account Successfully Created")
        return redirect("/SoundSphere/login/")
    return render(request,'music/signup.html')

# function for login system

def login(request):

    # check if the HTTP response is POST (form submission)   
    if request.method=="POST":
        username=request.POST.get("username") 
        password=request.POST.get("password")

        # if the user name is does not exist the show an error messaage

        if not User.objects.filter(username=username).exists():
            messages.info(request,"Invalid Username!")
            return redirect("/SoundSphere/login/")
    
        # authentication using password and the username

        user=authenticate(username=username,password=password)

        # if the authentication doesa not exist for the password

        if user is None:
            messages.info(request,"Invalid Password !")
            return redirect("/SoundSphere/login/")
     
        else:
        # for successful login 
           auth_login(request,user)
           return redirect("/SoundSphere/home/")
    return render(request,"music/login.html")

# for EachSongPage

def Songpage(request,idd):
    if not request.user.is_authenticated:
        return redirect('/SoundSphere/signup/')
    song=Song.objects.filter(song_id=idd).first()
    return render (request,"music/Songpage.html",{"Song":song} )
# function for all song 

def Allsongs(request):
    song=Song.objects.all()
    return render (request,"music/Allsongs.html",{"Song":song})
# function for each singer page

def Singerpage(request,sidd):
    singer_songs=Song.objects.filter(singer=sidd)
    number_of_songs=0
    for item in singer_songs:
         number_of_songs+=1
    song=Song.objects.all()
    singer_arr=[]
    for item in song:
        singer_arr.append(item.singer)
    singer_arr.sort()
    new_singer_arr=[]
    for element in singer_arr:
        if len(new_singer_arr)==0:
            new_singer_arr.append(element)
        if new_singer_arr[-1]!=element:
            new_singer_arr.append(element)      
    return render(request,"music/Singerpage.html",{"Song":singer_songs,"Singers": new_singer_arr,"number": number_of_songs})

def logout(request):
    if request.method=="POST":
        auth_logout(request)
        return redirect('/SoundSphere/login/')

    return render(request,"music/logout.html")

