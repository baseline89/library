from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        return self.name