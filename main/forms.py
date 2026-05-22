from django import forms
from .models import AdmissionApplication, ContactMessage, Course


class AdmissionForm(forms.ModelForm):
    class Meta:
        model  = AdmissionApplication
        fields = [
            'full_name', 'date_of_birth', 'gender', 'religion',
            'category', 'nationality', 'email', 'phone', 'address',
            'course_applied', 'academic_year',
            'tenth_percent', 'twelfth_percent', 'degree_percent', 'photo',
        ]
        widgets = {
            'full_name':      forms.TextInput(attrs={'placeholder': 'Full name as per certificate'}),
            'date_of_birth':  forms.DateInput(attrs={'type': 'date'}),
            'email':          forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone':          forms.TextInput(attrs={'placeholder': '+91 XXXXX XXXXX'}),
            'address':        forms.Textarea(attrs={'rows': 3, 'placeholder': 'Full postal address'}),
            'academic_year':  forms.TextInput(attrs={'placeholder': 'e.g. 2025-26'}),
            'tenth_percent':  forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01', 'min': '0', 'max': '100'}),
            'twelfth_percent':forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01', 'min': '0', 'max': '100'}),
            'degree_percent': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01', 'min': '0', 'max': '100'}),
            'religion':       forms.TextInput(attrs={'placeholder': 'Optional'}),
            'nationality':    forms.TextInput(attrs={'placeholder': 'Indian'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_applied'].queryset = Course.objects.filter(is_active=True)
        for field in self.fields.values():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing + ' form-control').strip()
        self.fields['photo'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-select'
        self.fields['course_applied'].widget.attrs['class'] = 'form-select'


class ContactForm(forms.ModelForm):
    class Meta:
        model  = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone':   forms.TextInput(attrs={'placeholder': '+91 XXXXX XXXXX'}),
            'subject': forms.TextInput(attrs={'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your message here...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'