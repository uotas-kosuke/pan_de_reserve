from django.shortcuts import render

def index(request):
    return render(request, 'pan_de_reserve/index.html')

def nyuryoku(request):
    return render(request, 'pan_de_reserve/nyuryoku.html')

def result(request):
    return render(request, 'pan_de_reserve/result.html')