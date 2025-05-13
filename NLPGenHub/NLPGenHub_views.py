from django.shortcuts import render
from rag_pipeline import ask_question  

def test(request):
    query=request.POST.get('question')
    document = request.POST.get('document')
    if document:
        print('Successfully uploaded!')

    if query:
        response = ask_question(query)
        return render(request, 'intelliqa.html', {'answer':response})
    else:
        return render(request, 'intelliqa.html', {'answer':"Please enter your question"})

    return render(request, "intelliqa.html")