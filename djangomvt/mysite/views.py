from django.shortcuts import render


def homePage(request):
    return render(request, 'home.html')
    # return HttpResponse("Привіт команда")

def about(request):
    return render(request, 'about.html')