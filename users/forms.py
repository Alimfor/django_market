from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from customers.models import Customer
from executers.models import Executor

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
            if user.user_type == '1':
                Customer.objects.create(user=user)
            elif user.user_type == '2':
                Executor.objects.create(user=user)
        return user
