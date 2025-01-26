from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import StudentForm
from .models import Student
from .models import Company
from .models import Olimpiad
from .models import LoginForm
from django.http import HttpResponse

j = 10
g_name = ''
g_second_name = ''
g_third_name = ''
g_genders = ''
g_bithday = ''
g_number = ''
g_email = ''
g_professia = ''
g_obrazovaniy = ''
g_dostyshenia = ''
g_dostyshenia_win = ''


def index_page(request):
    medal_g_dostyshenia_win = []
    all_student = Student.objects.all()

    medal = []

    if g_dostyshenia_win != "":
        medal_g_dostysheni_win = g_dostyshenia_win.split()
        for i in range(len(medal_g_dostysheni_win)):
            if medal_g_dostysheni_win[i].count(',') >= 1:
                medal_g_dostysheni_win[i] = medal_g_dostysheni_win[i][:-1]

        for i in medal_g_dostysheni_win:
            pobed = 0
            for j in all_student:
                if j.dostyshenia_win.count(i) >= 1:
                    pobed += 1
            print(i, pobed)
            for j in Olimpiad.objects.all():
                if j.nazv == i:
                    k = j.kolvo
            print(k)
            medal.append([i, 1, pobed, k])

        print(medal)

    companys = []
    for j in Company.objects.all():
        companys.append([j.name, j.description, j.metka])

    data = {'name': g_name,
            'second_name': g_second_name,
            'third_name': g_third_name,
            'genders': g_genders,
            'bithday': g_bithday,
            'number': g_number,
            'email': g_email,
            'professia': g_professia,
            'obrazovaniy': g_obrazovaniy,
            'dostyshenia': medal,
            'company': companys}

    # x.write(string)

    return render(request, 'test_index.html', context=data)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            all_students = Student.objects.all()
            have = False
            for i in all_students:
                if i.name == username:
                    global g_name, g_second_name, g_third_name, g_genders, g_bithday, g_number, g_email, g_professia, g_obrazovaniy, g_dostyshenia, g_dostyshenia_win
                    g_name = i.name
                    g_second_name = i.second_name
                    g_third_name = i.third_name
                    g_genders = i.genders
                    g_bithday = i.bithday
                    g_number = i.number
                    g_email = i.email
                    g_professia = i.professia
                    g_obrazovaniy = i.obrazovaniy
                    g_dostyshenia = i.dostyshenia
                    g_dostyshenia_win = i.dostyshenia_win
                    have = True
                    break
            if have:
                return redirect(index_page)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    return redirect(login_view)


def achievements(request):
    return render(request, 'profile.html')


def search(request):
    return render(request, 'search.html')


def companies(request):
    return render(request, 'companies.html')


def events(request):
    return render(request, 'events.html')


def bot(request):
    return render(request, 'bot.html')


def community(request):
    return render(request, 'community.html')
