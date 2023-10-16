from django import forms
class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    bf = forms.BooleanField(label="Вы согласны ?")
    nbf = forms.NullBooleanField(label="Точно согласны ?")
