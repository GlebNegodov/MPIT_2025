"""mpit_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import index_page
from app1.views import login_view
from app1.views import logout_view
from app1.views import achievements
from app1.views import search
from app1.views import companies
from app1.views import events
from app1.views import bot
from app1.views import community

urlpatterns = [
    path('', login_view),
    path('index/', index_page),
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
    path('achievements/', achievements),
    path('search/', search),
    path('companies/', companies),
    path('events/', events),
    path('bot/', bot),
    path('community/', community)
]
