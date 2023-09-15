from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, TemplateView

from . forms import ProfileForm
from . models import Bio
# Create your views here.






def home(request):
    return render(request, "home.html")


class ProfileView(DetailView):
    template_name = 'bio.html'
    model = Bio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

def logout_view(request):
    logout(request)
    return redirect('/')

class UserProfile(CreateView):
    model = Bio 
    form_class = ProfileForm
    template_name = 'bio.html'
    success_url = ''

        