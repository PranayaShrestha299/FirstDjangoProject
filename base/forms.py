from django.forms import ModelForm
from .models import Room
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  # This will include all fields from the Room model
        