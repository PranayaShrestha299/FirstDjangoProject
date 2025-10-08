from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User
class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude=['host']  # This will include all fields except host from the Room model

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Specify the fields you want to include