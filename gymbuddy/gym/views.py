from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_profile.models import Profile

@login_required
def homepage(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]
    if not profile.is_complete():
        return redirect('profile_update')
    return render(request, 'gym/index.html')

