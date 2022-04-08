from django.shortcuts import render
# for rendering HTML file
from subprocess import run,PIPE
import sys
import linkedinsearchengine

def button(request):
    return render(request,'home.html')
def output(request):
    if request.method == "POST":
        inp = request.POST.get('query')

        data = linkedinsearchengine.engine(inp)
        titles = []

        for i in range(0,len(data)-1):
            tit = data[i].title
            titles.append(tit)
    
    return render(request,'home.html',{'data':data})
