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
from django.contrib import admin
from django.urls import include, path

# The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
# The idea behind include() is to make it easy to plug-and-play URLs. Since displays are in their own URLconf (displays/urls.py), they can be placed under “/displays/”, or under “/fun_displays/”, or under “/content/displays/”, or any other path root, and the app will still work.
# You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.



urlpatterns = [
    # The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
    # path() argument: route - route is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches. 
    # Patterns don’t search GET and POST parameters, or the domain name.
    # path() argument: view - When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments. 
    # path() argument: kwargs - (optional) Arbitrary keyword arguments can be passed in a dictionary to the target view.
    # path() argument: name - (optional) Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

    # Points the root URLconf at the displays.urls module. In displays/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list.
    path("displays/", include('displays.urls')),
    # TODO: Add redirect for '' path
    # path('', include('displays.urls')),
    # Points to the default Admin page.
    path("admin/", admin.site.urls),
]
