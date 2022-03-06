from django.forms import ModelForm
from .models import SupportTickets

class SupportForm(ModelForm):
    class Meta:
        model = SupportTickets
        fields = "__all__"
        