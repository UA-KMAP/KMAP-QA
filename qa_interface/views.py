import fnmatch

from django.shortcuts import render,redirect
from django.http import Http404

from .models import QA_Interface

from .forms import QA_Form

from pathlib import Path
from datetime import date,datetime

from nltk.tokenize import sent_tokenize

import json,re,os.path
import pandas as pd 


#username='rakin061'  

def create_view(request):
	#print(request.GET)
	#print(request.POST)
	username=str(request.user)
	form=QA_Form(request.POST or None)

	print(form.is_valid())
	print(form.errors.as_data())



	if form.is_valid():
		form.save()
		form=QA_Form()
		
		author_id=request.POST['source_id']
		question=request.POST['question']
		answer=request.POST['answer']
		title_a=request.POST['title_A']
		par_A=script_context(request.POST['par_A'])
		title_b=request.POST['title_B']
		par_B=script_context(request.POST['par_B'])
		question_type=request.POST['question_type']
		level=request.POST['level']
		supporting_facts=request.POST['supporting_facts']
		insert_date=str(date.today())
		time=datetime.now().strftime('%I:%M %p')
		#print(question_id,question,answer,par_B,par_B,username,insert_date,time )

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
		    "id": author_id,
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

		#file_name=author_id+'_.json'
		directory_name="Dataset/"+username+"/"

		file_or_directory=Path(directory_name)

		if file_or_directory.exists():
			print("directory  exits---")
		else:
			file_or_directory.mkdir(parents=True, exist_ok=True)


		#Handling duplicate files for certain users...

		author_name_pattern = author_id + '*.json'

		for root, dirs, files in os.walk(directory_name):
			count_list = []
			for name in files:
				if fnmatch.fnmatch(name, author_name_pattern):
					count = name[-6]
					if count == "_":
						count_list.append(1)
					else:
						count_list.append(int(count) + 1)
			print(count_list)
			if not count_list:
				file_name = author_id + '_.json'
			else:
				file_name = author_id +'_'+ str(max(count_list)) + '.json'


		with open(directory_name+file_name, "w",encoding='utf-8') as outfile:
			json.dump(dictionary,outfile, ensure_ascii=False,indent=4)
			print("Json file writed..")

		return redirect('/create')

	else:

		data = pd.read_csv("KMAP_NLP_Dataset - Sample Dataset.csv")
		df = pd.DataFrame(data)
		#df=df.head(1)
		# df=df.fillna('Dr. Mark L. Brusseau is a professor in the School of Earth and Environmental Sciences at the University of Arizona, with joint appointments in the Soil, Water and Environmental Science Department and the Hydrology and Water Resources Department.')
		rand_row = df.sample()
		print(rand_row)
		param_a = rand_row['ParagraphA'].item()
		param_b = rand_row['ParagraphB'].item()
		title_a = rand_row['titleA'].item()
		title_b = rand_row['titleB'].item()
		source_id = rand_row['ID'].item()

		param_a_script=split_into_sentences_script(param_a)
		param_b_script=split_into_sentences_script(param_b)
		contribution=0

		directory_name="Dataset/"+username+"/"

		file_or_directory=Path(directory_name)

		if file_or_directory.exists():
			contribution=len([name for name in os.listdir(directory_name) if os.path.isfile(os.path.join(directory_name, name))])


		form=QA_Form(initial={'title_A':title_a,'title_B':title_b,'par_A': param_a_script,'par_B': param_b_script,"source_id":source_id})

		context={
			"form": form,
			"contribution": contribution,
			"username":username,
			"author_id":source_id
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
	sentences=' '.join(sentences)
	return sentences

def script_context(text):
	sentences = sent_tokenize(text)
	context_list=[]
	for sentence in sentences:
		context=sentence[4:]
		context_list.append(context)
	return context_list



