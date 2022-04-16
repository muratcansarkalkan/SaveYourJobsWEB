from django.shortcuts import render
# for rendering HTML file
from subprocess import run,PIPE
import sys
import json
import linkedinsearchengine
import os

def button(request):
    return render(request,'home.html')
def output(request):
    if request.method == "POST":
        inp = request.POST.get('query')
        data = linkedinsearchengine.engine(inp)
        jsonStr = json.dumps([i.__dict__ for i in data], indent=1)

        path = os.getcwd()
        with open('json_data.json', 'w') as outfile:
            outfile.write(jsonStr)

        f = (f'{path}\json_data.json')
        loader = json.load(open(f))
        # jobtitle = ([i["title"] for i in loader])
        # company = ([i["company"] for i in loader])
        # location =([i["location"] for i in loader])
        # link = [i["link"] for i in data]
    
    return render(request,'home.html',{'loader':loader})