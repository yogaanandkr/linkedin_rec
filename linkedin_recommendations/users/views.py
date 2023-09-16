from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from allauth.account.signals import user_signed_up  
from django.dispatch import receiver

from . forms import ProfileForm
from . models import Bio, User, Recommendations
# Create your views here.




@receiver(user_signed_up)
def create_bio_for_user(sender, request, user, **kwags):
    if not Bio.objects.filter(user = user).exists():
        Bio.objects.create(user = user)

    return render(request, 'home.html')


def home(request):
    return render(request, "home.html")


# def profiles(request):
#     profiles = Bio.objects.all()
#     return render(request, "profiles.html", {
#         'profiles': profiles
#     })
def profiles(request):
    user = request.user
    profiles = Bio.objects.exclude(user = request.user)
    print(profiles)
    # profiles = Bio.objects.all()
    user = User.objects.get(username = request.user.username)
    current_user = Bio.objects.get(user = user)
    return render(request, 'profiles.html', {
        'user' : user,
        'profiles' : profiles,
        'current_user': current_user,
    })

def logout_view(request):
    logout(request)
    user = request.user

    return redirect('/')

def userdetail(request, name):
    user = User.objects.get(username = name)
    profile = Bio.objects.get(user = user)
    recommendations = Recommendations.objects.filter(recommended_user = user.username)

    if Recommendations.objects.filter(recommended_by = request.user.username, recommended_user = user.username).exists() or (user.username == request.user.username):
        display = 'none'

    else:
        display = 'block'

    
    return render(request, 'bio.html', {
        'profile' : profile,
        'recommendations' : recommendations,
        'display': display
        # 'recommended_by_id' : recommended_by_id

    })
        

def recommend(request):
    if request.method == 'POST':
        c_user = request.POST['c_user']
        v_user = request.POST['v_user']
        v_user_obj = User.objects.get(username = v_user)

        print('=============================================================================')
        # print(v_user_obj.id)
        recommendation = request.POST['recommendation']

        new_recommendation = Recommendations.objects.create(recommended_by = c_user, recommended_user = v_user, recommendation = recommendation)
        new_recommendation.save()

        return redirect('profile/'+ str(v_user_obj.username))