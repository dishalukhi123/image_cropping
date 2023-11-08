

from django.db import models



class Question(models.Model):
    question_id = models.AutoField
    question_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date =models.DateField()



