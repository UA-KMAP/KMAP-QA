from django.db import models
from django.urls import reverse


# Create your models here.

class QA_Interface(models.Model):
	
	#ource_id=models.CharField(max_length=20,blank=False,null=False) # max_length = required
	par_A=models.TextField(blank=False, null=False)
	par_B=models.TextField(blank=False, null=False)
	question=models.TextField(blank=False, null=False, max_length=200)
	answer=models.TextField(blank=False, null=False, max_length=100)


	question_type_choices= [('Bridge_entity', 'Bridge'),('Comparison', 'Comparison'),('Intersection', 'Intersection'),('Commonsense_reasoning', 'Commonsense')]
	question_type=models.CharField(max_length=22, choices=question_type_choices, default='Bridge_entity')

	level_choices=[('Hard','Hard'),('Medium','Medium'),('Easy','Easy')]
	level=models.CharField(max_length=6, choices=level_choices, default='Easy')

    #question_type=models.CharField(max_length=12, choices=question_type_choices,default='Bridge_entity')
	#price=models.DecimalField(decimal_places=2, max_digits=10000)
	supporting_facts=models.TextField(blank=False, null=False,max_length=4)
	#featured=models.BooleanField(default=True) # null=True, default=True


	def get_absolute_url(self):
		return reverse("qa:qa_entity", kwargs={"id":self.id}) 
