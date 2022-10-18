from django.shortcuts import render

# Create your views here.
def vidiopembelajaran(request):
    vidiopembelajaran = "Vidiopembelajaran"
    gambaranumum = "materi"

    konteks = {
        'vidiopembelajaran': vidiopembelajaran,
        'gbrumum': gambaranumum,
    }
    return render(request, 'vidiopembelajaran.html', konteks)