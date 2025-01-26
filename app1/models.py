from django.db import models
from django import forms
from django.utils.timezone import now


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=35)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.second_name


class Student(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=35)
    third_name = models.CharField(max_length=35)
    passoword = models.CharField(max_length=35, default=1234)
    genders = models.CharField(max_length=35)
    bithday = models.DateField()
    number = models.IntegerField(default=8)
    # salary = models.IntegerField(default=0)
    email = models.CharField(max_length=35)
    professia = models.CharField(max_length=35)
    obrazovaniy = models.CharField(max_length=35)
    telega = models.CharField(max_length=35, default='')
    dostyshenia = models.CharField(max_length=100, default='', blank=True)
    dostyshenia_win = models.CharField(max_length=100, default='', blank=True)
    sorev = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.second_name


class Olimpiad(models.Model):
    nazv = models.CharField(max_length=35)
    kolvo = models.IntegerField(default=12900)
    vrem = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.nazv


class StudentForm(forms.Form):
    name = forms.CharField(label='name')
    second_name = forms.CharField(label='second_name')
    third_name = forms.CharField(label='third_name')
    passoword = forms.CharField(label='passoword')
    genders = forms.CharField(label='genders')
    bithday = forms.DateField(label='bithday')
    number = forms.IntegerField(label='number')
    # salary = models.IntegerField(default=0)
    email = forms.CharField(label='email')
    professia = forms.CharField(label='professia')
    obrazovaniy = forms.CharField(label='obrazovaniy')
    dostyshenia = forms.CharField(label='dostyshenia')


class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=35)
    metka = models.BooleanField(default=False)
    telega = models.CharField(max_length=35, default='')
