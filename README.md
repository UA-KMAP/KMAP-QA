

                                     =====================================
                                      QA Interface for Institutional Data
                                     =====================================


# Question Answering Interface

QA dataset for institutional data that requires reasoning over multiple documents, and does so in natural language, without constraining itself to an existing knowledge base or schema. The goal is to collect a diverse and explainable question answering dataset similar to [HotpotQA](https://huggingface.co/datasets/hotpot_qa/viewer) but limited to only institutional research data. As it is non-trivial to collect text based multi-hop questions a specific data collection pipeline and data annotation mechanism has been designed to predict the correct answer to a question that requires multiple reasoning ‘hops’ across given contexts as institutional data. 

# Data Collection Pipeline

For the collection of the dataset our primary corpus will be the research data from the University of Arizona. And the data collection pipeline for our dataset will be performed by crowd sourcing where multiple supporting context documents will be shown and asked explicitly to come up with questions requiring reasoning over those contexts such as paragraphs, tables, profiles etc. This ensures coverage of multi-hop questions that are more natural and are not designed with any pre-existing knowledge base schema in mind.



# Example of Multi-hop Questions: 

Multi-hop questions require systems to aggregate information between multiple contexts, the ability of a system to reason over various sources of institutional data such as Google Scholar, University faculty websites and output desired answer. Similarly multi-step reasoning has been perfomred by a model if it reaches one or more intermediate conclusions before concluding the final answer and each of the intermediate
conclusions serves as a necessary premise for the next one. This sequence of intermediate and the
final conclusions is called a reasoning chain and Each reasoning step of the reasoning chain can be termed as a hop.

### [Chcek the image...](https://github.com/Rakin061/Smart-Weather-Agent/blob/master/static/Screenshot.png)


        # Multihop What is the population of the capital city of Bangladesh  ?
        # Answer: 40 Millions !!
        # Reasoning: Capital City of Bangladesh: Dhaka ---> Population: 40 Millions
        .............

 

# Requirements 

        #asgiref==3.5.2
        #click==8.1.3
        #Django==4.1.2
        #joblib==1.2.0
        #nltk==3.8.1
        #numpy==1.23.4
        #pandas==1.5.1
        #python-dateutil==2.8.2
        #pytz==2022.6
        #regex==2022.10.31
        #six==1.16.0
        #sqlparse==0.4.3
        #tqdm==4.64.1

# Dependencies

        #Python >= 3.8
        #Django >= 4.1.x
        #NLTK >=3.8.1

### Download NLTK Data
* `pip install nltk`
* `python -m nltk.downloader popular`

### It is highly encouraged to run the application in virtual environment. 


# Installation:

## Dev Server:

### Clone the Repository:
* `git clone https://github.com/UA-KMAP/KMAP-QA.git`


### Create Virtual Environment and install dependencies listed in requirements.txt
* `python3 -m venv virtualenv`
* `source virtualenv/bin/Activate`
* `pip3 install -r requirements.txt`

### Run the Server from terminal or other configuration environment
* `python3 manage.py runserver`


# Structure of the dataset

The top level structure of each JSON file is a list, where each entry represents a question-answer data point. Each data point is
a dict with the following keys:
- `_id`: a unique id for this question-answer data point. This is useful for evaluation.
- `question`: a string.
- `answer`: a string. The test set does not have this key.
- `supporting_facts`: a list. Each entry in the list is a list with two elements `[title, sent_id]`, where `title` denotes the title of the 
paragraph, and `sent_id` denotes the supporting fact's id (0-based) in this paragraph. The test set does not have this key.
- `context`: a list. Each entry is a paragraph, which is represented as a list with two elements `[title, sentences]` and `sentences` is a list
of strings.

There are other keys that are not used in our code, but might be used for other purposes (note that these keys are not present in the test sets, and your model should not rely on these two keys for making preditions on the test sets):
- `type`: either `comparison` or `bridge`, indicating the question type. (See our paper for more details).
- `level`: one of `easy`, `medium`, and `hard`. (See our paper for more details).

### *** The dataset will be stored in the direcotry Dataset/{username} as json data per contributions. 

# Functionalities:

1. Login Screen. No registrations required. Credentials will be provided manually. 
2. QA interface will be consists of multiple paragraphs from original corpus. 
3. Support for **Data records** added for distinct users..
4. Conversation Refreshing option
5. User can see their overall contributions.
6. Conversation Archiving and monitoring.
7. Failed Response tracking added..

# Regards, 

Developer : Salman Rakin

# References: 

The original paper for HotpotQA is [here](https://arxiv.org/abs/1809.09600) and the [homepage](https://hotpotqa.github.io/) and github repository for this dataset can be found [here](https://github.com/hotpotqa/hotpot).  
	