from django.db import models

# Create your models here.
"""
class Post(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	status = models.ChoiceField( 
		Zaplanirovana="Zaplanirovana",
		Vypolneno="Vypolneno",
		Otmeneno="Otmeneno"
		)
	choice_status = models.CharField(max_length=50, choices = status, default= "Zaplanirovana")
	def __str__(self):
		return (self.title)
"""


class Zadacha(models.Model):
	Opisanie = models.CharField(max_length=150)
	zz = 'Zaplanirovana'
	vv = 'Vypolneno'
	oo = 'Otmeneno'
	choice_status = (
			(zz,'Zaplanirovana'),
			(vv, 'Vypolneno'),
			(oo, 'Otmeneno')
		)
	status = models.CharField(max_length=100, choices = choice_status)

class Quote(models.Model):
	quote = models.CharField(max_length=255)
	quote_author = models.CharField(max_length=255)
	ss = 'Today'
	z = 'Tomorrow'
	p = 'After three days'
	choise_quote = (
			(ss, 'Today'),
			(z, 'Tomorrow'),
			(p, 'After three days')
		)
	chytaty = models.CharField(max_length=100, choices = choise_quote)