from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from user_profile.models import Profile
from django.views import View


@login_required
def homepage(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]
    if not profile.is_complete():
        return redirect('profile_update')
    return render(request, 'gym/index.html')

class ChatAdvice(LoginRequiredMixin, View):
    template_name = 'gym/chat_advice.html'
    def get(self, request, *args, **kwargs):
        user_profile = Profile.objects.get(user=request.user)
        chat_advice = user_profile.get_chat_advice()
        return render(request, self.template_name, {'chat_advice': chat_advice})
    
class ChatView(View):
    template_name = 'gym/chat.html'
    def get(self, request, *args, **kwargs):
        user_profile = Profile.objects.get(user=request.user)
        chat_advice = user_profile.get_chat_advice()
        return render(request, self.template_name, {'chat_advice': chat_advice})