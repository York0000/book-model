from django.db import models


class StaffModel(models.Model):
    image = models.ImageField(upload_to='staff')
    name = models.CharField(max_lefrom django.db import models


class StaffModel(models.Model):
    image = models.ImageField(upload_to='staff')
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    info = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'
