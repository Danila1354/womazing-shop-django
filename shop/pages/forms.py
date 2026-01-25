from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        verbose_name = "Обращения"
        verbose_name_plural = "Обращения"
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": " "}),
            "email": forms.EmailInput(attrs={"class": "form-input", "placeholder": " "}),
            "phone": forms.TextInput(attrs={"class": "form-input", "placeholder": " "}),
            "message": forms.Textarea(attrs={"class": "form-input", "placeholder": " ", "rows": 4}),
        }

    