from django.db import models
from django.urls import reverse


# Create your models here.

class QA_Interface(models.Model):
	
	source_id=models.CharField(max_length=30,blank=False,null=False) # max_length = required
	title_A=models.CharField(blank=False, null=False,max_length=35)
	par_A=models.TextField(blank=False, null=False)
	title_B=models.CharField(blank=False, null=False,max_length=35)
	par_B=models.TextField(blank=False, null=False)
	question=models.TextField(blank=False, null=False, max_length=1000)
	answer=models.TextField(blank=False, null=False, max_length=100)


	question_type_choices= [('Bridge_entity', 'Bridge'),('Comparison', 'Comparison'),('Intersection', 'Intersection'),('Commonsense_reasoning', 'Commonsense')]
	question_type=models.CharField(max_length=22, choices=question_type_choices, default='Bridge_entity')

	level_choices=[('Hard','Hard'),('Medium','Medium'),('Easy','Easy')]
	level=models.CharField(max_length=6, choices=level_choices, default='Easy')

    #question_type=models.CharField(max_length=12, choices=question_type_choices,default='Bridge_entity')
	#price=models.DecimalField(decimal_places=2, max_digits=10000)
	supporting_facts=models.TextField(blank=False, null=False,max_length=4, help_text=' &nbsp; <button type="button" class="btn btn-info" data-bs-container="body" '
																					  'data-bs-toggle="popover" data-bs-placement="right" data-bs-html="true" '
																					  'data-bs-content="Supporting facts specify the sentences involved while creating the multi hop question from '
																					  'both of the paragraphs.<br> <b>Example Input: 0,1. </b> It indicates that first sentence from the first paragraph and '
																					  'second sentence from the second paragraph have been used to produce the multi hop question.. <a href='' title=''test add link'' >  "> ? </button>')
	#featured=models.BooleanField(default=True) # null=True, default=True


	def get_absolute_url(self):
		return reverse("qa:qa_entity", kwargs={"id":self.id}) 
