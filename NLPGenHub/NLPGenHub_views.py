from django.http import HttpResponse
from django.shortcuts import render
from rag_pipeline import load_data, vectorstore, ask_question
from .forms import UploadFileForm
from .models import QueryData
import hashlib
import os

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
        form = UploadFileForm(request.POST, request.FILES) #Instantiate the Django form 
        file = request.FILES.get('query_file')
        query=request.POST.get('question')

        if file:
            file_hash = get_file_hash(file)
            if QueryData.objects.filter(file_hash=file_hash).exists():
                return render(request, "intelliqa.html", {'form':form,
                    'answer':f"Duplicate file detected, file named \
                    already present"})
            
            form_data = QueryData.objects.create(query_file=file, file_hash=file_hash)
            form_data.save()
            file_path = 'media/NLP_data/' + os.path.basename(form_data.query_file.name)
            print(f"File path------->:",file_path)
            raw_text = load_data(file_path)
            vectorstore_db = vectorstore(persist_directory='media/NLP_data/chroma_db',texts=raw_text)
            return render(request, "intelliqa.html", {'form':form})
        
        elif query:
            vectorstore_db = vectorstore(persist_directory='media/NLP_data/chroma_db')
            response = ask_question(query,vectorstore_db)
            return render(request, 'intelliqa.html', {'answer':response,'form':form})
        else:
            return render(request, 'intelliqa.html', {'answer':"Please enter your question"})
    
    else:
        form = UploadFileForm()
    return render(request, "intelliqa.html", {'form':form})