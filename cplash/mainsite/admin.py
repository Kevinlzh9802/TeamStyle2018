# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User
from .models import Student
from .models import Team

class TeamAdmin(admin.ModelAdmin):
	list_display=('name','leader')

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Team,TeamAdmin)
# Register your models here.
