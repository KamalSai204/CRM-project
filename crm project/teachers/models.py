from django.db import models
class Teachers(models.Model):
    image=models.ImageField(upload_to="teachers/",blank=True,null=True)
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=20)   
def __str__(self):
    return self.name