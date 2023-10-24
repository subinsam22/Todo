from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name


class Links(models.Model):
    address=models.CharField(max_length=250,null=True,blank=True)
    string_name=models.CharField(max_length=250,null=True,blank=True)


    # def __str__(self):
    #     return self.string_name