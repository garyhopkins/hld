from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Display

# Functions that are called from the URLS.py file

# It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provides a shortcut for this using render().
# The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional 
# third argument. It returns an HttpResponse object of the given template rendered with the given context.

# Gets iterable object and passes to index template so it can be iterated through
def index(request):
    displays = Display.objects.order_by('display_name')
    # print(displays)
    # print(type(displays))
    return render(request, 'displays/index.html', {'displays': displays})

# It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut for this using get_object_or_404().
# The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.
# Why do we use a helper function get_object_or_404() instead of automatically catching the ObjectDoesNotExist exceptions at a higher level, or having the model API raise Http404 instead of ObjectDoesNotExist?
# Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the django.shortcuts module.

# Gets single, non iterable object for a single display and passes to template so it can be displayed
def detail(request, display_uuid):
    displays = get_object_or_404(Display, pk=display_uuid)
    # print(displays)
    # print(type(displays))
    return render(request, 'displays/detail.html', {'displays': displays})

# Displays the create_display template which has a form to submit a new display record
def create(request):
    return render(request, 'displays/create.html')