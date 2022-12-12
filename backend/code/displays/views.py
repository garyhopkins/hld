from django.shortcuts import render
from django.http import HttpResponse

# Function that is called from the urls.py file... can be named anything, doesn't have to be index
def index(request):
    response = "<H1><span style=""color:#84be3f"">This is the displays route. Display listings will show on this page.</span> <br><br><span style=""color:red"">Need template with a form to submit a new display.</span>"
    return HttpResponse(response)
