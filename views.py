from django.shortcuts import render

def submit(request):
    return render(request, 'submit.html')

def show_exam_result(request):
    return render(request, 'exam_result.html')
