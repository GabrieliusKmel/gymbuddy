from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from . import models, forms
from django.utils.translation import gettext_lazy as _
from django.template.loader import get_template
from django.views import View
from weasyprint import HTML
from django.utils import timezone
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
@csrf_protect
def profile_update(request: HttpRequest):
    if request.method == "POST":
        profile_form = forms.ProfileUpdateForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
                user_profile = request.user.profile
                if 50 < user_profile.height <= 300 and 30 < user_profile.weight <= 300 and 10 < user_profile.age <= 100:
                    profile_form.save()
                    if not user_profile.chat_advice:
                        messages.success(request, _('Your first GymBuddy is generating! Please wait..'))
                        return redirect('chatadvice')
                    else:
                        time_now = timezone.now()
                        time_left = user_profile.time_left - time_now
                        time_left_formatted = f"{time_left.seconds // 3600} hours and {(time_left.seconds // 60) % 60} minutes"
                        if user_profile.time_left < time_now:
                            messages.success(request, _('Your GymBuddy is generating! Please wait..'))
                            return redirect('profile_update')
                        else:
                            messages.error(request, _(f'You can generate GymBuddy again in {time_left_formatted}'))
                            return redirect('profile_update')
                else:
                    messages.error(request, _(f'The weight can be from 30 to 300 kg, the height from 50 to 300 cm, and the age from 10 to 100 years.'))
        else:
            messages.error(request, _('The weight can be from 30 to 300 kg, the height from 50 to 300 cm, and the age from 10 to 100 years.'))
    else:
        profile_form = forms.ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user_profile/update.html', {
        'profile_form': profile_form,
    })

def profile(request: HttpRequest):
    return render(request, "user_profile/profile.html")

@csrf_protect
def signup(request: HttpRequest):
    if request.method == "POST":
        errors = []
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not len(username) > 3 or User.objects.filter(username=username).exists():
            errors.append(_('Username is already taken, or is too short.'))
        if not len(email) > 0 or User.objects.filter(email=email).exists():
            errors.append(_('Email must be valid and not belonging to an existing user.'))
        if not len(password1) > 7 or password1 != password2:
            errors.append(_('Password is too short, or entered passwords do not match.'))
        if len(errors):
            for error in errors:
                messages.error(request, error)
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            profile = models.Profile(user=user)
            profile.save()
            messages.success(request, _("Sign up successful. You can log in now."))
            return redirect('login')
    return render(request, 'user_profile/signup.html')

class GeneratePDF(View):
    template_name = 'user_profile/pdf.html'

    def get_context_data(self):
        user_profile = models.Profile.objects.get(user=self.request.user)
        chat_advice = user_profile.get_chat_advice()
        return {'chat_advice': chat_advice}

    def get(self, request, *args, **kwargs):
        template = get_template(self.template_name)
        context = self.get_context_data()
        html = template.render(context)
        pdf_file = HTML(string=html).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="gymbuddy.pdf"'
        return response