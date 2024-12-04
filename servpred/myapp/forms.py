from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Clase CSS para Bootstrap
            'placeholder': 'Nombre de Usuario',  # Placeholder para el input
            'required': True,  # Campo requerido
        })
    )
    correo = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',  # Clase CSS para Bootstrap
            'placeholder': 'Correo Electrónico',  # Placeholder para el input
            'required': True,  # Campo requerido
        })
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  # Clase CSS para Bootstrap
            'placeholder': 'Contraseña',  # Placeholder para el input
            'required': True,  # Campo requerido
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  # Clase CSS para Bootstrap
            'placeholder': 'Confirmar Contraseña',  # Placeholder para el input
            'required': True,  # Campo requerido
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'correo']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',  
            'placeholder': 'Correo Electrónico', 
            'required': True, 
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  
            'placeholder': 'Contraseña',  
            'required': True, 
        })
    )

