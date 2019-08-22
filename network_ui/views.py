from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'home.html')
