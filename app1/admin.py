from django.contrib import admin
from app1.models import Worker
from app1.models import Student
from app1.models import Olimpiad
from app1.models import Company

# Register your models here.
admin.site.register(Worker)
admin.site.register(Student)
admin.site.register(Olimpiad)
admin.site.register(Company)
