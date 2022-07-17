from pyexpat import model
from sre_parse import Verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length = 30, verbose_name="Full Name",blank= False)
    dob = models.DateField()
    physics = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    chemistry = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    maths = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    cs = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])

    @property
    def agg(self):
        pc = (((self.physics + self.chemistry + self.maths + self.cs)*100)/400)
        return pc
        print(pc)

    class Meta: 
        verbose_name = 'Student Marksheet'
        ordering = ["-name"]

    def __str__(self):
        return self.name

