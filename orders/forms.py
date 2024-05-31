from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['deadline'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        
        

    class Meta:
        model = Order
        fields = ['title', 'description', 'service', 'price']


