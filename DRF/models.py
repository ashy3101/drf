from django.db import models

class model_data(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

    def __str__(self):
        self.first_name