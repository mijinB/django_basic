from django.db import models


class CommonModel(models.Model):
    """Model Definition for Common"""

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
