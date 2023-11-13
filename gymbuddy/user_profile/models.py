from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import generate_chat_advice_task
from django.utils import timezone
from datetime import timedelta


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
    chat_advice_time = models.DateTimeField(_("Chat advice time"), null=True, blank=True)
    time_left = models.DurationField(_("Time left until next advice generation"), null=True, blank=True)


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
    
    def set_chat_advice_time(self, time):
        self.chat_advice_time = time
        self.save()
    
    def set_time_left(self, time_left):
        if not hasattr(self, '_setting_time_left'):
            self._setting_time_left = True
            self.time_left = time_left
            self.save()
            delattr(self, '_setting_time_left')
    
@receiver(post_save, sender=Profile)
def generate_chat_advice(sender, instance, created, **kwargs):
    if created or not instance.get_chat_advice():
        if instance.is_complete():
            generate_chat_advice_task.delay(instance.pk)
    else:
        time_since_last_generation = timezone.now() - instance.chat_advice_time
        time_left = timedelta(hours=24) - time_since_last_generation
        if not hasattr(instance, '_setting_time_left'):
            instance.set_time_left(time_left)