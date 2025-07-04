from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rag_pipeline import load_data, vectorstore, ask_question
from .forms import UploadFileForm
from .models import QueryData
import hashlib
import os
import json
import requests


def get_file_hash(file_obj):
    sha256 = hashlib.sha256()
    for chunk in file_obj.chunks():
        sha256.update(chunk)

    return sha256.hexdigest()

def test(request):

    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key 
    print(f"Session_id:", session_id)

    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)          #Instantiate the Django form 
        file = request.FILES.get('query_file')                      #Upload file 
        query=request.POST.get('question')                          # User question    

        if file:
            file_hash = get_file_hash(file)
            if QueryData.objects.filter(file_hash=file_hash).exists():
                duplicate_file = QueryData.objects.get(file_hash=file_hash)    #fetching model instance QueryData
                return render(request, "intelliqa.html", {'form':form,
                    'answer':f"Duplicate file detected, \
                        file named {os.path.basename(duplicate_file.query_file.name)} \
                            already present in the system."})
            
            request.session['file_count'] = request.session.get('file_count', 0)

            if (request.session['file_count']) > 4:
                return render(request, 'intelliqa.html',\
                              {'answer':"Upload limit of 5 files reached for this session.", 'form':form})
            
            form_data = QueryData.objects.create(query_file=file, file_hash=file_hash)
            form_data.save()
            file_path = 'media/NLP_data/' + os.path.basename(form_data.query_file.name)
        
            request.session['file_count'] += 1
    
            raw_text = load_data(file_path)
            vectorstore_db = vectorstore(persist_directory='media/NLP_data/chroma_db',texts=raw_text)
            return render(request, "intelliqa.html", {'form':form})
        
        elif query:
            if not os.path.exists('media/NLP_data/chroma_db'):
                return render(request, 'intelliqa.html', {' answer':"No file uploaded. Please upload a file to proceed.", 'form':form})
            vectorstore_db = vectorstore(persist_directory='media/NLP_data/chroma_db')
            response = ask_question(query,vectorstore_db)
            return render(request, 'intelliqa.html', {'answer':response,'form':form})
        else:
            return render(request, 'intelliqa.html', {'answer':"Please enter your question",'form':form})
    
    else:
        form = UploadFileForm()
    return render(request, "intelliqa.html", {'form':form})


def intent_classify(request):

    API_URL = 'https://25hvdlk3p0.execute-api.us-east-1.amazonaws.com/prod/intent_classify'

    if request.method=='POST':
        prompt = request.POST.get('prompt')
        payload = {"input": f"Classify the intent: {prompt}"}
        headers = {"Content-Type": "application/json"}


        try:
            response = requests.post(API_URL,json=payload,headers=headers)
            response_data = json.loads(response.text)
            return render(request, "supportiq.html", {"response":response_data})
        
        except requests.exceptions.HTTPError as e:
            return render(request, "supportiq.html", {"error":f"API Error: {str(e)}"})
        
        except Exception as e:
            return render(request, "supportiq.html", {"error": f"Unexcepted Error: {str(e)}"})

    return render(request, "supportiq.html")
        