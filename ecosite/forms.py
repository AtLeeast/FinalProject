from django import forms


class BottlesFoundForm(forms.Form):
    # amount = forms.IntegerField()
    image = forms.FileField()
