from django.shortcuts import render,redirect
from .models import Url
from django.http import HttpResponse
import uuid

# Create your views here.

def index(request):
    return render(request,"base.html")

def create(request):
    if request.method == "POST":
        link = request.POST["link"]
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
def go(request,pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect("https://"+url_details.link)