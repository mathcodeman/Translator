from django.shortcuts import render
from .translate import trans
# Create your views here.

def translator_view(request):
    
    if request.method == "POST":
        o_text = request.POST['my_textarea']
        output = trans(o_text)
        return render(request,'translator.html',{'output_text':output,'original_text':o_text})
    else:
        return render(request,'translator.html')