from django.db import models

# Create your models here.
class StudentFlow(models.Model):
	department = models.CharField(max_length=128)
	flow_type = models.CharField(max_length=16)
	category = models.CharField(max_length=16)
	batch = models.CharField(max_length=8)
	year = models.CharField(max_length=2)
	major_from = models.CharField(max_length=128)
	code_from = models.CharField(max_length=16)
	status = models.CharField(max_length=128)
	college_to = models.CharField(max_length=128)
	major_to = models.CharField(max_length=128)
	code_to = models.CharField(max_length=16)
	number = models.IntegerField()