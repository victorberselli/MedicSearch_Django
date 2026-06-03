from django.http import HttpResponse
from medicSearch.models import Profile

def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")

    return HttpResponse("<h1>Lista de médicos!</h1>")

    medics = Profile.objects.all()
    print(medics)