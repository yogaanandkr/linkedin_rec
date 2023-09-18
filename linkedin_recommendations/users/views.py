from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from allauth.account.signals import user_signed_up  
from django.dispatch import receiver
from django.urls import reverse_lazy    

from . forms import ProfileForm
from . models import Bio, User, Recommendations, Posts, Follow
# Create your views here.




@receiver(user_signed_up)
def create_bio_for_user(sender, request, user, **kwags):
    if not Bio.objects.filter(user = user).exists():
        Bio.objects.create(user = user)
        Posts.objects.create(user = user)

    return render(request, 'home.html')



def home(request):
    all_posts = Posts.objects.all().order_by('-created_at')
    print(all_posts)
    return render(request, "home.html", {
        'all_posts' : all_posts
    })


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
    recommendations = Recommendations.objects.filter(recommended_user = user.username).order_by('-id')
    if Follow.objects.filter(user = name).exists():
        follower_count = len(Follow.objects.filter(user = name))
        button_text = 'Unfollow'
    else:
        follower_count = 0
        button_text = 'Follow'

    if Recommendations.objects.filter(recommended_by = request.user.username, recommended_user = user.username).exists() or (user.username == request.user.username):
        display = 'none'

    else:
        display = 'block'

    
    return render(request, 'bio.html', {
        'profile' : profile,
        'recommendations' : recommendations,
        'display': display,
        'follower_count' : follower_count,
        'button_text' : button_text
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
        # if (Recommendations.objects.filter(recommended_by  = c_user, recommended_user = v_user, recommendation = recommendation)).exists():
        #     edit_recommendation = Recommendations.objects.filter(recommended_by  = c_user, recommended_user = v_user, recommendation = recommendation)
        #     edit_recommendation.recommendation = recommendation
        #     edit_recommendation.delete()

        # else:
        new_recommendation = Recommendations.objects.create(recommended_by = c_user, recommended_user = v_user, recommendation = recommendation)
        new_recommendation.save()

        return redirect('profile/'+ str(v_user_obj.username))
    
def edit_rec_page(request, id):
    rec = Recommendations.objects.get(id = id)

    return render(request, 'edit_recommendation.html', {
        'rec': rec
    })


def rec_edit(request):
    if request.method == 'POST':
        id = request.POST['id']
        ex_rec = Recommendations.objects.get(id = id)
        edited_rec = request.POST['editrecommendation']
        ex_rec.recommendation = edited_rec
        ex_rec.save()
        return redirect('profile/' + ex_rec.recommended_user)
    

def rec_delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        # recommended_userr = None
        ex_rec = Recommendations.objects.get(id = id)
        recommended_userr = ex_rec.recommended_user
        ex_rec.delete()
        return redirect('profile/' + recommended_userr)
    

def get_profile_form(request, name):
    name = User.objects.get(username = name)
    bio = Bio.objects.get(user = name)
    return render(request, 'edit_bio.html', {
        'bio' : bio
    })

def updateprofile(request):
    if request.method == "POST":
        name = request.POST['name']
        bio = request.POST['bio']
        user = User.objects.get(username = name)
        update_bio = Bio.objects.get(user = user)

        
        if request.FILES.get('image') != None:
            image = request.FILES['image']
            update_bio.bio = bio 
            update_bio.profile_pic = image 
            update_bio.save()
            return redirect('profile/' + name)
        
        if request.FILES.get('image') == None:
            image = update_bio.profile_pic
            update_bio.bio = bio 
            update_bio.profile_pic = image 
            update_bio.save()
            return redirect('profile/' + name)
        
        




# class BioDetailView(DetailView):
#     template_name = 'edit_bi0.html'
#     model = Bio

#     def get_object(self, queryset=None):
#         name = self.kwargs.get('name')  # Get the 'name' parameter from the URL
#         return get_object_or_404(Bio, user = name)

# class ProfileUpdateView(UpdateView):
#     model = Bio 
#     form_class = ProfileForm
#     template_name = 'edit_bio.html'
    
#     def get_object(self, queryset = None):
#         bio_id = self.kwargs.get('bio_id')
#         return get_object_or_404(Bio, id = bio_id)
    
#     def get_success_url(self) -> str:
#         return reverse_lazy('profile', kwargs={'username': self.request.user.username})


def upload_post(request):
    if request.method == "POST":
        image = request.FILES['post']
        caption = request.POST['caption']
        create_post = Posts.objects.create(user = request.user, post_img = image, caption = caption)
        create_post.save()
        return redirect('home')
    return render(request, 'upload_post.html')


def follow(request):
    if request.method == "POST":
        user = request.POST['user']
        follower = request.user.username

        if Follow.objects.filter(follower = follower, user = user).exists():
            delete_follow = Follow.objects.get(follower = follower, user = user)
            delete_follow.delete()
        
        else:
            create_follow = Follow.objects.create(follower = follower, user = user)
            create_follow.save()
        
        return redirect('profile/' + user)
