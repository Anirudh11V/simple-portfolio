from django.forms import ModelForm
from .models import feedback

class feedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'