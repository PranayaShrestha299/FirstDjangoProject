from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Room
from .forms import RoomForm
from .models import Topic

# Create your views here.

#rooms = [
#    {'id': 1, 'name': 'Room A'},
#    {'id': 2, 'name': 'Room B'},
#    {'id': 3, 'name': 'Room C'}, ]

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__icontains=q) 
    topics=Topic.objects.all()
    context = {'rooms': rooms,'topics':topics} # 'rooms' is the variable name used in the template
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
    

