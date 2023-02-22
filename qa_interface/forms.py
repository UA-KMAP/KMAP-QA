from django import forms

from .models import QA_Interface

class QA_Form(forms.ModelForm):
	class Meta: 
		print("Form Data")
		model=QA_Interface
		widgets = {
          'par_A': forms.Textarea(attrs={'rows':5, 'cols':125}),
          'par_B': forms.Textarea(attrs={'rows':5, 'cols':125}),
          'question': forms.Textarea(attrs={'rows':2, 'cols':100, 'placeholder': 'Enter a multi hop question from the above two paragraphs....'}),
          'answer': forms.Textarea(attrs={'rows':1, 'cols':100,'placeholder':'Enter the answer ...' }),
          'supporting_facts':forms.Textarea(attrs={'rows':1, 'cols':5}),
          #'source_id': forms.HiddenInput(),
        }
        
		fields= [
			#"source_id",
			"par_A",
			"par_B",
			"question",
			"answer",
			"question_type",
			"level",
			"supporting_facts"

		]

		labels = {
           'par_A' : '',
           'par_B' : '',
           'question' : 'Question',
           'answer' : '_Answer_',
        }
