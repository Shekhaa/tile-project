from django.http import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect("home/index")
#Njh2SHch_vAWPPgBevt8V61tiZBQg9YigLYRQtTdR