# -*- coding: utf-8 -*-
from django import forms
from mainsite import models

class LoginForm(forms.Form):
	user_name = forms.CharField(label='用户名:',max_length=20)
	user_password = forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput)

	def __unicode__(self):
		return self.user_name

class  RegisterForm(forms.Form):
	user_name = forms.CharField(label='用户名:',max_length=20)
	user_password = forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput)
	user_email = forms.EmailField(label='电子邮件')

	def __unicode__(self):
		return self.user_name

class AddTeam(forms.Form):
	team_name = forms.CharField(label='队名',max_length=20)
	team_leader = forms.CharField(label='队长',max_length=20,required=False,widget=forms.TextInput(attrs={'type': 'hidden'}))
	team_code = forms.CharField(label='邀请码',max_length=8)
	def __unicode__(self):
		return self.team_name
		