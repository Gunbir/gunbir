from django.db import models

# Create your models here.
class Activity(models.Model):
	state=models.BooleanField(default=False)
	quantity=models.IntegerField()
	name=models.CharField(max_length=200)
	ids=models.IntegerField()
	update=models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.name
