from django.http import HttpResponse
from django.shortcuts import render
from rag_pipeline import load_data, vectorstore, ask_question
from .forms import UploadFileForm
from .models import QueryData


def upload_file(request):
    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES.get('query_file')
        form_data = QueryData.objects.create(query_file=file)
        form_data.save()
        return HttpResponse("Successfully uploaded file")
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form':form})

def test(request):

    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    print(f"Session_id:", session_id)

    form = UploadFileForm()

    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES.get('query_file')
        query=request.POST.get('question')

        if file:
            form_data = QueryData.objects.create(query_file=file)
            form_data.save()
            print('Successfully uploaded!')
            raw_text = load_data(path='media/NLP_data')
            vectorstore_db = vectorstore(raw_text)
            return render(request, "intelliqa.html", {'form':form})
        
        elif query:
            raw_text = load_data(path='media/NLP_data')
            vectorstore_db = vectorstore(raw_text)
            response = ask_question(query,vectorstore_db)
            return render(request, 'intelliqa.html', {'answer':response,'form':form})
        else:
            return render(request, 'intelliqa.html', {'answer':"Please enter your question"})
    

    return render(request, "intelliqa.html", {'form':form})