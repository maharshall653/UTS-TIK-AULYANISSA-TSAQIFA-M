from django.shortcuts import render

# Create your views here.
def latihan(request):
    latihan = "Latihan"
    gambaranumum = "latihan"

    konteks = {
        'latihan': latihan,
        'gbrumum': gambaranumum,
    }
    return render(request, 'latihan.html', konteks)