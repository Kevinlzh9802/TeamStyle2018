# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	template = get_template('home.html')
	html = template.render(locals())

	return HttpResponse(html)