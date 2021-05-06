from .models import Group
from django.forms import ModelForm


class GroupCreationForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'prize', 'about']
