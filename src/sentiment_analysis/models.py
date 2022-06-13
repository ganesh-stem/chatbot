from django.db import models
from django.urls import reverse
# Create your models here.

class SA(models.Model):
    input_sentence = models.CharField(max_length=100, blank=False, null=False)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
