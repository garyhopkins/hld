"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


# How does Django differentiate the URL names between them? For example, the displays app has a detail view, and so might a blog app that is in the same project. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?
# The answer is to add namespaces to your URLconf. Use app_name to set the application namespace.

app_name = 'displays'
urlpatterns = [

    # Path will call the index function in views.py.
    path('', views.index, name='index'),

    # Path will call the detail function in views.py, passing the display UUID that is included in the URL.
    # The 'name' value is called by the {% url %} template tag. This way you don't have to hardcode the URL into the template.
    path('<uuid:display_uuid>/', views.detail, name='detail'),

    # Path will call the create function in views.py.
    path('create/', views.create, name='create'),

    # Path will call the delete function in views.py.
    path('delete/<uuid:display_uuid>/', views.delete, name='delete'),

    # Path will call the update function in views.py
    path('<uuid:display_uuid>/update/', views.update, name="update"),

    # Path will call the display_list function in views.py
    path('results/', views.results, name="results"),
]
