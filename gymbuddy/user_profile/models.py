from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _

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
    gender = models.CharField(_("gender"), max_length=10, choices=(
        ("male", _("Male")),
        ("female", _("Female")),
    ), null=True, blank=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    
    def is_complete(self):
        return self.height is not None and self.weight is not None and self.gender is not None