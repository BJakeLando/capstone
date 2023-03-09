from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .models import Profile, Peep
from django.contrib import messages
from .forms import PeepForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin

def profileHome(request):
    if request.user.is_authenticated:
        form = PeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                peep = form.save(commit=False)
                peep.user = request.user
                peep.save()
                messages.success(request, ("Your Peep has been posted!"))
                return redirect('profileHome')

        peeps = Peep.objects.all().order_by("-created_at")
        return render(request, 'accounts/profileHome.html', {"peeps": peeps, "form": form})
    else:
        peeps = Peep.objects.all().order_by("-created_at")
        return render(request, 'accounts/profileHome.html', {"peeps": peeps})
    
class EditProfileView(LoginRequiredMixin, UpdateView):
    template_name ="accounts/editprofile.html"
    model = Profile
    fields = ["profile_image"]

    success_url = reverse_lazy('vlist')

    def updateProfile(self, request):
        form = ProfileForm(request.POST, request.FILES)

        context = {
            'form': form
        }
        if form.is_valid():
            form.save()

        return render(request, 'vlog/vlist.html', context)

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
        peeps = Peep.objects.filter(user_id=pk).order_by('-created_at')
        form = PeepForm(request.POST or None)
        
        if request.method == "POST":
                if form.is_valid():
                    peep = form.save(commit=False)
                    peep.user = request.user
                    peep.save()
                    messages.success(request, ("Your Peep has been posted!"))
                    return redirect('profileHome')
            
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

        peeps = Peep.objects.all().order_by("-created_at")
        return render(request, "accounts/profile.html", {'profile': profile, "peeps": peeps,'form': form,})
    else:
        messages.success(request, ("you must be logged in to view this page"))
        return redirect('home')
