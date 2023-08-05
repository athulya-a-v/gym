from django import forms
from .models import UploadRoutine

class RoutineSelectionForm(forms.Form):
    routine = forms.ModelChoiceField(queryset=UploadRoutine.objects.all())