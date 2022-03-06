from django.forms import ModelForm
from .models import SupportTickets

class SupportForm(ModelForm):
    class Meta:
        model = SupportTickets
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'