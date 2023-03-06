from django.db import models
from django.urls import reverse


# Create your models here.

class QA_Interface(models.Model):
	
	source_id=models.CharField(max_length=30,blank=False,null=False) # max_length = required
	title_A=models.CharField(blank=False, null=False,max_length=35)
	# par_A_mod=models.TextField(blank=False, null=False)
	par_A=models.TextField(blank=False, null=False)
	title_B=models.CharField(blank=False, null=False,max_length=35)
	# par_B_mod=models.TextField(blank=False, null=False)
	par_B = models.TextField(blank=False, null=False)
	question=models.TextField(blank=False, null=False, max_length=1000,help_text=' &nbsp; <button type="button" class="btn btn-danger btn-sm align-top" data-bs-container="body" '
																					  'data-bs-toggle="popover" data-bs-placement="right" data-bs-html="true"  '
																					  'data-bs-content=" Multi-hop questions require systems to aggregate information between '
																				      'multiple contexts, the ability of a system to reason over multiple sources of '
																				      'data such as paragraphs to output desired answer. Here, the system has to reason with information taken from more than one document '
																				      '(i.e. Parapgaphs) to arrive at the final answer. <br> <br> <b> Example: </b> What is the population of the capital city of Bangladesh ? '
																				      '<br> <b>Answer: </b> 40 Millions !!'
																				 	  '<br> <b>Reasoning:</b> Capital City of Bangladesh ---> Dhaka ---> Population: 40 Millions. '
																				      '<br> <br> Click <a href='' https://hotpotqa.github.io/ '' '
																				      'target=''_blank'' > here </a> to see further details of multihop questions ! "> ? </button>')
	answer=models.TextField(blank=False, null=False, max_length=100)


	question_type_choices= [('Bridge_entity', 'Bridge'),('Comparison', 'Comparison'),('Intersection', 'Intersection'),('Commonsense_reasoning', 'Commonsense')]
	question_type=models.CharField(max_length=22, choices=question_type_choices, default='Bridge_entity',help_text=' &nbsp; <button type="button" class="btn btn-danger btn-sm align-top" data-bs-container="body" '
																					  'data-bs-toggle="popover" data-bs-placement="right" data-bs-html="true"  '
																					  'data-bs-content=" Types of multi hop question you entered. Click <a href='' https://github.com/UA-KMAP/KMAP-QA/blob/main/qa_interface/templates/images/MHQA.png '' '
																				      'target=''_blank''> here </a> to see details of different types of multi hop question. "> ? </button>')

	level_choices=[('Hard','Hard'),('Medium','Medium'),('Easy','Easy')]
	level=models.CharField(max_length=6, choices=level_choices, default='Easy', help_text=' &nbsp; <button type="button" class="btn btn-danger btn-sm align-top" data-bs-container="body" '
																					  'data-bs-toggle="popover" data-bs-placement="right" data-bs-html="true"  '
																					  'data-bs-content="Difficulty level of the multi hop question you entered! "> ? </button>' )

    #question_type=models.CharField(max_length=12, choices=question_type_choices,default='Bridge_entity')
	#price=models.DecimalField(decimal_places=2, max_digits=10000)
	supporting_facts=models.TextField(blank=False, null=False,max_length=4, help_text=' &nbsp; <button type="button" class="btn btn-danger btn-sm align-top" data-bs-container="body" '
																					  'data-bs-toggle="popover" data-bs-placement="right" data-bs-html="true"  '
																					  'data-bs-content="Supporting facts specify the sentences involved while creating the multi hop question from '
																					  'both of the paragraphs.<br> <b>Example Input: 0,1. </b> It indicates that first sentence from the first paragraph and '
																					  'second sentence from the second paragraph have been used to produce the multi hop question.."> ? </button>')
	#featured=models.BooleanField(default=True) # null=True, default=True


	def get_absolute_url(self):
		return reverse("qa:qa_entity", kwargs={"id":self.id}) 
