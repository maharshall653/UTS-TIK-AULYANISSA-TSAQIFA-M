from django.shortcuts import render

# Create your views here.
def home(request):
    home = "Home"
    gambaranumum = "home"

    konteks = {
        'home': home,
        'gbrumum': gambaranumum,
    }
    return render(request, 'home.html', konteks)