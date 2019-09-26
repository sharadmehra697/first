from django.db import models

# Create your models here.
class first(models.Model):
	first_id=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=20)