from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Order, UserProfile


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_type", "title", "description", "price"]

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order

    def delete(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.delete()
        return order


class UserRegistrationForm(UserCreationForm):
    USER_CHOICES = [
        ("customer", "Заказчик"),
        ("executor", "Исполнитель"),
    ]
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )
    phone_number = forms.CharField(
        label="Номер телефона",
        max_length=15,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Номер телефона"}
        ),
    )
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Фамилия"}
        ),
    )

    user_type = forms.ChoiceField(choices=USER_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Имя пользователя"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Подтверждение пароля"}
        )
        self.fields["user_type"].widget.attrs.update(
            {"class": "form-select form-control"}
        )

        # Добавляем классы Bootstrap для меток
        self.fields["username"].label = "Имя пользователя"
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Подтверждение пароля"
        self.fields["user_type"].label = "Тип пользователя"

        # Прижимаем метки вправо
        self.fields["username"].label_suffix = ""
        self.fields["password1"].label_suffix = ""
        self.fields["password2"].label_suffix = ""
        self.fields["user_type"].label_suffix = ""
        self.fields["email"].label_suffix = ""
        self.fields["phone_number"].label_suffix = ""

        # Добавляем классы Bootstrap для ошибок
        self.fields["username"].error_messages = {
            "required": "Это поле обязательно для заполнения"
        }
        self.fields["password1"].error_messages = {
            "required": "Это поле обязательно для заполнения"
        }
        self.fields["password2"].error_messages = {
            "required": "Это поле обязательно для заполнения"
        }
        self.fields["user_type"].error_messages = {
            "required": "Это поле обязательно для заполнения"
        }
        self.fields["email"].error_messages = {
            "required": "Это поле обязательно для заполнения"
        }
        self.fields["phone_number"].error_messages = {
            "required": "Это поле обязательно для заполнения"
        }

    def save(self, commit=True):
        user = super().save(commit=commit)  # Сохраняем пользователя в базе данных
        # Создаем профиль пользователя и связываем его с созданным пользователем
        user_profile = UserProfile.objects.create(
            user=user,
            phone=self.cleaned_data["phone_number"],
        )  # Создаем профиль пользователя и сохраняем в него номер телефона
        user_profile.user.email = self.cleaned_data["email"]
        user_profile.user.first_name = self.cleaned_data["first_name"]
        user_profile.user.last_name = self.cleaned_data["last_name"]
        user_profile.user.save()
        return user