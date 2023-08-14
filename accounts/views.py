from django.shortcuts import render, redirect, reverse
from .models import Profile, Address
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm, SignUpForm
# TODO: don't forget the page_title attribute


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('login'))
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'page_title': 'SignUp',
    }
    return render(request, 'registration/signup.html', context=context)


# define get function that get user profile details
@login_required
def profile_details(request, *args, **kwargs):
    queryset = Profile.objects.get(user=request.user)
    context = {
        'profile': queryset,
        'page_title': f"Aviato | Profile"
    }
    return render(request, 'profile-details.html', context)


# define update function that edit user profile
@login_required
def update_profile(request, *args, **kwargs):
    queryset = Profile.objects.get(user_id=request.user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile-details'))
    form = UpdateProfileForm
    context = {
        'from': form,
        'page_title': 'Aviato | Update profile',
    }
    return render(request, 'update-profile.html', context)
