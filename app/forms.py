from django import forms

class AddVideoForm(forms.Form):
    file_path = forms.FileField()


    