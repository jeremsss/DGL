from django.db import models

class Submisyon(models.Model):
	fnam = models.CharField(blank = True, max_length=100)
	emayl = models.CharField(blank = True, max_length=100)
	seks = models.CharField(blank = True, max_length=100)
	countri = models.CharField(blank = True, max_length=100) 
	descr = models.CharField(blank = True, max_length=100)
class Digitaltype(models.Model):
	tda = models.CharField(blank = True, max_length=100)
	reso = models.CharField(blank = True, max_length=100)
	orient = models.CharField(blank = True, max_length=100)
	nameart = models.CharField(blank = True, max_length=100)
	prays = models.IntegerField(blank = True)
	curr = models.CharField(blank = True, max_length=100)

class Devicedused(models.Model):
	mayn = models.CharField(blank = True, max_length=100)
	sekond = models.CharField(blank = True, max_length=100)
	brando = models.CharField(blank = True, max_length=100)
	modelo = models.CharField(blank = True, max_length=100)


	



