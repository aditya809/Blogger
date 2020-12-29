from django import forms 
from .models import *
  
class Blogform(forms.ModelForm): 
	
	class Meta: 
		model = Blogs

		fields = ['title', 'short_description','image_photo','url'] 
	# title = models.CharField(max_length=100)
	# short_description = models.TextField(max_length=200)
	# image_photo = models.ImageField(upload_to='images/',default='NULL') 
	# url = models.URLField()


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
