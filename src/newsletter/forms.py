from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
		class Meta:
				model = SignUp
				fields = ['full_name','email']
				### exclude = [] use sparingly 

		def clean_email(self):
			email = self.cleaned_data.get('email')
			email_base, provider = email.split("@")
			domain, extension = provider.split('.')
			if not extension == "co":
					raise forms.ValidationError("pls use a viald email address yo")
			return email