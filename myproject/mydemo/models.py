from django.db import models




class student (models.Model):
    student_id = models.AutoField
    student_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date =models.DateField()
    student_Email = models.EmailField()
