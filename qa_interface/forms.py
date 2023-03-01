from django import forms

from .models import QA_Interface

class QA_Form(forms.ModelForm):
	class Meta: 
		print("Form Data")
		model=QA_Interface
		widgets = {
		  'title_A':forms.TextInput(attrs={'size':'20','class':'title'}),
          'par_A': forms.Textarea(attrs={'rows':2, 'cols':140,'class':'paragraph'}),
          'title_B':forms.TextInput(attrs={'size':'20','class':'title'}),
          'par_B': forms.Textarea(attrs={'rows':2, 'cols':140,'class':'paragraph'}),
          'question': forms.Textarea(attrs={'rows':1, 'cols':100,'class':'question', 'placeholder': 'Enter a multi hop question from the above two paragraphs....'}),
          'answer': forms.Textarea(attrs={'rows':1, 'cols':100,'class':'answer','placeholder':'Enter the answer ...' }),
          'supporting_facts':forms.Textarea(attrs={'rows':1, 'cols':5}),
          'source_id': forms.HiddenInput(),
        }
        
		fields= [
			"source_id",
			"title_A",
			"par_A",
			"title_B",
			"par_B",
			"question",
			"answer",
			"question_type",
			"level",
			"supporting_facts"

		]

		labels = {
		   'title_A':'',
		   'title_B':'',
           'par_A' : '',
           'par_B' : '',
           'question' : 'Question',
           'answer' : '_Answer_',
        }

