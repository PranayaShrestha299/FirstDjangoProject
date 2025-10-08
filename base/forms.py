from django.forms import ModelForm
from .models import Room
class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude=['host']  # This will include all fields except host from the Room model
        