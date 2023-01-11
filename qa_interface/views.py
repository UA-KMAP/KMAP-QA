from django.shortcuts import render,redirect
from django.http import Http404

from .models import QA_Interface

from .forms import QA_Form

from pathlib import Path
from datetime import date,datetime

from nltk.tokenize import sent_tokenize

import json,re,os.path
import pandas as pd 

# Create your views here.

#username='rakin061'  

def create_view(request):
	print(request.GET)
	print(request.POST)
	username=str(request.user)
	form=QA_Form(request.POST or None)

	print(form.is_valid())

	data=pd.read_csv("KMAP_NLP_Dataset - Sample Dataset.csv")
	df = pd.DataFrame(data)
	#df=df.head(100)
	#df=df.fillna('Dr. Mark L. Brusseau is a professor in the School of Earth and Environmental Sciences at the University of Arizona, with joint appointments in the Soil, Water and Environmental Science Department and the Hydrology and Water Resources Department.')
	rand_row=df.sample()
	print(rand_row)
	param_a=rand_row['ParagraphA'].item()
	param_b=rand_row['ParagraphB'].item() 
	title_a=rand_row['titleA'].item()
	title_b=rand_row['titleB'].item()
	source_id= rand_row['ID'].item()
	

	if form.is_valid():
		form.save()
		form=QA_Form()
		
		question_id=request.POST['csrfmiddlewaretoken']
		question=request.POST['question']
		answer=request.POST['answer']
		par_A=split_into_sentences(param_a)
		par_B=split_into_sentences(param_b)
		question_type=request.POST['question_type']
		level=request.POST['level']
		supporting_facts=request.POST['supporting_facts']
		insert_date=str(date.today())
		time=datetime.now().strftime('%H:%M:%S')  
		print(question_id,question,answer,par_B,par_B,username,insert_date,time )

		sentences=[par_A,par_B]
		supporting_facts=supporting_facts.split(',')
		supporting_facts= list(map(int,supporting_facts))



		supporting_facts={
			"title":[ title_a, title_b ], 
			"sent_id": supporting_facts
		}

		context={
			"title":[ title_a,title_b ], 
			"sentences": sentences
		}



		dictionary = {
		    "id": source_id,
		    "Question": question,
		    "Answer": answer,
		    "type":question_type,
		    "level":level,
		    "supporting_facts":supporting_facts,
		    "context":context,
		    "User_name":username,
		    "Date":insert_date,
		    "time":time,
		}
		
		#json_object = json.dumps(dictionary, indent=4)

		file_name=question_id+'_.json'
		directory_name="Dataset/"+username+"/"

		file_or_directory=Path(directory_name)

		if file_or_directory.exists():
			print("directory  exits---")
		else:
			file_or_directory.mkdir(parents=True, exist_ok=True)

		with open(directory_name+file_name, "w",encoding='utf-8') as outfile:
			json.dump(dictionary,outfile, ensure_ascii=False,indent=4)
			print("Json file writed..")

		return redirect('/create')

	else: 

		param_a_script=split_into_sentences_script(param_a)
		param_b_script=split_into_sentences_script(param_b)
		contribution=0

		directory_name="Dataset/"+username+"/"

		file_or_directory=Path(directory_name)

		if file_or_directory.exists():
			contribution=len([name for name in os.listdir(directory_name) if os.path.isfile(os.path.join(directory_name, name))])


		form=QA_Form(initial={'par_A': param_a_script,'par_B': param_b_script,"source_id":source_id})

		context={
			"form": form,
			"contribution": contribution,
			"username":username
		}
		return render(request,"qa_create.html",context)


def detail_view(request):
	obj=QA_Interface.objects.all()
	contribution=0
	username=str(request.user)

	directory_name="Dataset/"+username+"/"

	file_or_directory=Path(directory_name)

	if file_or_directory.exists():
		contribution=len([name for name in os.listdir(directory_name) if os.path.isfile(os.path.join(directory_name, name))])

	context={
		"elements": obj,
		"contribution": contribution,
		"username":username

	}
	return render(request,"detail.html",context)

def delete_view(request,id):
	try:
		obj=QA_Interface.objects.get(id=id)
		obj.delete()
		return redirect('/elements')
	except QA_Interface.DoesNotExist:
		raise Http404


def dynamic_view(request,id):
	try:
		obj=QA_Interface.objects.get(id=id)
	except QA_Interface.DoesNotExist:
		raise Http404

	context={
		"element": obj,
		"id":id,
	}
	return render(request,"entity.html",context)


def split_into_sentences_script(text):
	sentences = sent_tokenize(text)
	i=0
	for s in sentences:
		sentences[i]='['+str(i)+'] '+s
		i=i+1

	sentences = [s.strip() for s in sentences]
	return sentences

def split_into_sentences(text):
	sentences = sent_tokenize(text)
	return sentences
