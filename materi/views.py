from django.shortcuts import render

# Create your views here.
def materi(request):
    materi = "Materi"
    gambaranumum = "materi"

    konteks = {
        'materi': materi,
        'gbrumum': gambaranumum,
    }
    return render(request, 'materi.html', konteks)