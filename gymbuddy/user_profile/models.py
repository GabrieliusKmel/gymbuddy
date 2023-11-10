from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from openai import OpenAI
from tinymce.models import HTMLField

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name="profile",
        null=True, blank=True
    )
    height = models.FloatField(_("height"), null=True, blank=True)
    weight = models.FloatField(_("weight"), null=True, blank=True)
    age = models.PositiveIntegerField(_("age"), null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=10, choices=(
        ("male", _("Male")),
        ("female", _("Female")),
    ), default="male")
    activity_level = models.CharField(_("activity level"), max_length=100, choices=(
        ("sedentary", _("Sedentary")),
        ("light", _("Light")),
        ("moderate", _("Moderate")),
        ("active", _("Active")),
        ("very_active", _("Very Active")),
    ), default="sedentary")
    weight_goal = models.CharField(_("weight goal"), max_length=100, choices=(
        ("gain_weight", _("Gain Weight")),
        ("stay_lean", _("Stay Lean")),
        ("cut", _("Cut")),
    ), default="gain_weight")

    chat_advice = models.TextField(_("ChatGPT advice"), null=True, blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

    def is_complete(self):
        return (
            self.height is not None and
            self.weight is not None and
            self.age is not None and
            self.gender is not None and
            self.activity_level is not None and
            self.weight_goal is not None
        )

    def set_chat_advice(self, advice):
        self.chat_advice = advice
        self.save()

    def get_chat_advice(self):
        return self.chat_advice
    
@receiver(post_save, sender=Profile)
def generate_chat_advice(sender, instance, created, **kwargs):
    if created or not instance.get_chat_advice():
        if instance.is_complete():
                client = OpenAI(
                    api_key="",
                )
                conversation = f"User Profile:\nHeight: {instance.height} cm.\nWeight: {instance.weight} kg.\nAge: {instance.age} years old.\nGender: {instance.get_gender_display()}\nActivity Level: {instance.get_activity_level_display()}\nWeight Goal: {instance.get_weight_goal_display()}"
                messages = [
                    {
                        "role": "system",
                        "content": "Be super straightforward and simple. You are the good trainer and nutritionist. Give a detailed meal plan with calories count and a detailed workout plan in the gym with reps count for the given user profile data and rest plan. Don't write that you were given this data. Just give the answer.",
                    },
                    {
                        "role": "user",
                        "content": conversation,
                    }
                ]
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                chat_response = response.choices[0].message.content.strip()
                instance.set_chat_advice(chat_response)