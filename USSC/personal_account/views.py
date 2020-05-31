from django.shortcuts import render


def index(request):
    return render(request, 'personal_account/personal_account.html')
