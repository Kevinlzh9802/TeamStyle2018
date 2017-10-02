# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from mainsite import forms
from .models import User
from .models import Team

# Create your views here.
def homepage(request):
	if 'username' in request.session:
		username = request.session['username']
		useremail = request.session['useremail']
		message = username+useremail
	template = get_template('home.html')	
	#if request.session.test_cookie_worked():
	#	request.session.delete_test_cookie()
	#	message = "cookie supported!"
	#else:
	#	message = "cookie not supported"
	#request.session.set_test_cookie()
	html = template.render(locals())

	return HttpResponse(html)

def login(request):
	username = 0
	flag = False
	if 'username' in request.session:
		flag = True
		username = request.session['username']
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			username=request.POST['user_name']
			userpass=request.POST['user_password']
			message="登录成功"+username
			try:
				user = User.objects.get(name=username)
				if user.password == userpass:
					flag = True
					response = redirect('/')
					request.session['username'] = user.name
					request.session['useremail'] = user.email
					return response
				else:
					message = "wrong password"
			except:
				message = "error"
		else:
			message="请检查"
#		username=request.POST['user_name']
#		userpass=request.POST['user_password']
#		message=username
	else:
		login_form = forms.LoginForm()
	template = get_template('login.html')
#	if 'username' in request.COOKIES:
#		username = request.COOKIES['username']
	response = HttpResponse(render(request,'login.html',locals()))
#	try:	
#		if username : response.set_cookie('username',username)
#		if userpass: response.set_cookie('userpass',userpass)
#	except:
#		pass
	return response

def logout(request):
	response = redirect('/')
	request.session.pop('username')
	request.session.pop('useremail')
	return response

def register(request):
	if request.method == 'POST':
		reg_form = forms.RegisterForm(request.POST)
		if reg_form.is_valid():
			username=request.POST['user_name']
			userpass=request.POST['user_password']
			useremail=request.POST['user_email']
			message="注册成功,"+username
			if username != None:
				all_user = User.objects.all()
				flag = True
				for one in all_user:
					if one.name == username or one.email == useremail:
						flag = False
						break
					else:
						pass
				if flag:
					user = User.objects.create(name=username,password=userpass,email=useremail)
					user.save()
					return redirect('/')
				else:
					message="the user exist!"
			else:
				pass
		else:
			message="请检查"
	else:
		reg_form = forms.RegisterForm()

	
	template = get_template('register.html')
	
	response = HttpResponse(render(request,'register.html',locals()))
	return response

def rule(request):
	if 'username' in request.session:
		flag = True
		username = request.session['username']
	template = get_template('rule.html')
	return HttpResponse(template.render(locals()))

def team(request):
	if 'username' in request.session:
		flag = True
		username = request.session['username']
	template = get_template('team.html')
	team = Team.objects.all()
	if team:
		message = "队伍信息如下："
	return HttpResponse(template.render(locals()))

def add_team(request):
	if 'username' in request.session:
		flag = True
		username = request.session['username']
	if request.method == 'POST':
		add_form = forms.AddTeam(request.POST)
		if add_form.is_valid():
			tname=request.POST['team_name']
			tcode=request.POST['team_code']
			message="成功,"+tname
			if tname != None:
				all_team = Team.objects.all()
				user = User.objects.all()
				flag = True
				message += tname
				for one in all_team:
					message += one.name
					if one.name == tname:
						message="the team exist!"
						flag = False
						break
					elif str(one.leader) == username:
						message="您已拥有一支队伍!"
						flag = False
						break
					elif tcode == one.code:
						message="邀请码已存在"
						flag = False
						break
					else:
						pass
				if flag :
					new = Team.objects.create(name=tname,leader=User.objects.get(name=username))
					new.save()
					message = "创建成功"
					#return redirect('/team')
				else:
					pass
			else:
				pass
		else:
			message="请检查"
	else:
		add_form = forms.AddTeam()	
	template = get_template('AddTeam.html')
	response = HttpResponse(render(request,'AddTeam.html',locals()))
	return response

def show_team(request,username):
	#username = request.session['user_name']
	team = Team.objects.all()
	template = get_template('ShowTeam.html')
	for one in team:
		if str(one.leader) == username:
			myteam = one
		else:
			pass
	return HttpResponse(template.render(locals()))