from django.http import HttpResponse


def home(request):
    return HttpResponse("It will be site with recipes")
