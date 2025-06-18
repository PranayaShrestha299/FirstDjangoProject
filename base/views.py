from django.contrib import messages
from multiprocessing import context
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Room
from .forms import RoomForm
from .models import Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#rooms = [
#    {'id': 1, 'name': 'Room A'},
#    {'id': 2, 'name': 'Room B'},
#    {'id': 3, 'name': 'Room C'}, ]

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Logic to authenticate user goes here
        try:
            user = User.objects.get(username=username)  
        
        except :
            # User does not exist
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password is incorrect')
    context={}
    return render(request,'base/login_register.html',context)

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(description__icontains=q))
    topics=Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms,'topics':topics,'room_count':room_count} # 'rooms' is the variable name used in the template
    return render(request, 'base/home.html',context)

def about(request):
    return render(request, 'about.html')

def room(request,pk):
    room=Room.objects.get(id=pk)
    context = {'room': room}  # 'room' is the variable name used in the template
    return render(request, 'base/room.html', context)
def createroom(request):
    form=RoomForm();
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form': form}
    return render(request, 'base/room_form.html',context)

def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteroom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
   
    return render(request, 'base/delete.html', {'obj':room})



    

