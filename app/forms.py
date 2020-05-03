from django import forms
from .models import AcctModel,KeywordModel

class AcctForm(forms.ModelForm):
    passwd = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AcctModel
        fields = '__all__'
       
class KeywordForm(forms.ModelForm):
    class Meta:
        model = KeywordModel
        fields = '__all__'