# -*- coding: utf-8 -*-    
from __future__ import unicode_literals

from django.db import models
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=20,null=False)
	email = models.EmailField()
	password = models.CharField(max_length=20,null=False)
	enabled = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class Student(models.Model):
	SEX = (
		('B','Boy'),
		('G','Girl'),
		)
	name = models.CharField(max_length = 200)
	student_ID = models.CharField(max_length =10)
	sex = models.CharField(max_length = 10, choices=SEX)

	def __unicode__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=20,default="none",verbose_name="名称")
	leader = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)

	code = models.CharField(max_length=8,verbose_name="邀请码",null =False,default="00000000")

	def __unicode__(self):
		return self.name