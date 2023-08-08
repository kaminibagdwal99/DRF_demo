from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    roll_number = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.first_name+ " "+ self.last_name