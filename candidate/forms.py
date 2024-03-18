from django import forms

class ProfileForm(forms.Form):
    title = forms.CharField(max_length=200)
    experience = forms.FloatField()
    location = forms.CharField(max_length=250)
    min_salary = forms.DecimalField(max_digits=10,decimal_places=2)
    comf_salary = forms.DecimalField(max_digits=10,decimal_places=2)
    birth_date = forms.DateField()
    tags = forms.CharField()