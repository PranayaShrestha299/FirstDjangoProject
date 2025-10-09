from django.forms import ModelForm
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude=['host']  # This will include all fields except host from the Room model

class CustomUserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']  # Specify the fields you want to include

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # your custom user model
        fields = ['username', 'email']  # include the fields you want in the registration form