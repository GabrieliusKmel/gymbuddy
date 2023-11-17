from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from tinymce.models import HTMLField

class AboutUs(models.Model):
    content = HTMLField(_("content"), max_length=10000, default='', blank=True)

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("aboutus_detail", kwargs={"pk": self.pk})

