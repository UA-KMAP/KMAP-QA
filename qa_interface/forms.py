from django import forms

from .models import QA_Interface


class QA_Form(forms.ModelForm):
    class Meta:
        print("Form Data")
        model = QA_Interface
        widgets = {
            'title_A': forms.TextInput(attrs={'class': 'title'}),
            # 'par_A_mod': forms.Textarea(attrs={'rows': 2, 'cols': 140, 'class': 'paragraph'}),
            'par_A': forms.HiddenInput(),
            'title_B': forms.TextInput(attrs={'class': 'title'}),
            # 'par_B_mod': forms.Textarea(attrs={'rows': 2, 'cols': 140, 'class': 'paragraph'}),
            'par_B': forms.HiddenInput(),
            'question': forms.Textarea(attrs={'rows': 1, 'cols': 100,'class': 'question',
                                              'placeholder': 'Enter a multi hop question from the above two paragraphs....'}),
            'answer': forms.Textarea(
                attrs={'rows': 1, 'cols': 30, 'class': 'answer', 'placeholder': 'Enter the answer ...'}),
            'supporting_facts': forms.Textarea(attrs={'rows': 1, 'cols': 5}),
            'source_id': forms.HiddenInput(),
        }

        fields = [
            "source_id",
            "title_A",
            "par_A",
            # "par_A_mod",
            "title_B",
            "par_B",
            # "par_B_mod",
            "question",
            "answer",
            "question_type",
            "level",
            "supporting_facts"

        ]

    # labels = {
    #    'title_A':'',
    #    'title_B':'',
    #    'par_A' : '',
    #    'par_B' : '',
    #    'question' : 'Question',
    #    'answer' : '_Answer_',
    # }
