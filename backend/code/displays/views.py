from django.shortcuts import render
from django.http import HttpResponse

# Function that is called from the urls.py file... can be named anything, doesn't have to be index
def index(request):
    response = "<H1><span style=""color:#8de820;border-style:dotted;"">This is the displays route. Display listings will show on this page.</span> <br><br><span style=""color:red"">TODO: Template with a form to submit a new display.</span>"
    return HttpResponse(response)
