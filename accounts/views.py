from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .models import Profile, Peep
from django.contrib import messages


def profileHome(request):
    if request.user.is_authenticated:
        peeps = Peep.objects.all()
    return render(request, 'accounts/profileHome.html', {"peeps": peeps})
    
    
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name= "registration/signup.html"
    success_url = reverse_lazy('login')


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'accounts/profiles.html', {'profiles': profiles})
    else:
        messages.success(request, ("you must be logged in to view this page"))
        return redirect('home')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)

        # Post Form Logic
        if request.method == 'POST':
            current_user_profile = request.user.profile
        # Get Form Data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # Save the profile
            current_user_profile.save()
        return render(request, "accounts/profile.html", {'profile': profile})
    else:
        messages.success(request, ("you must be logged in to view this page"))
        return redirect('home')