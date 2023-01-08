#CS50x (Fall 2022) Final Project - HolidayLightDisplays website

## Description:

This is my final project for CS50x. It is a website where users can find holiday light displays, such as those for Christmas, Halloween, etc. Users can view a list of the displays that are added and they can also add a new display. It also contains the ability to edit an existing display and mark one as deleted if need be. All data is stored within a SQLite database.

The site is quite simple for now, however I already have several more enhancements that I plan on implementing (Detailed below)

## Tech stack:

- Python
- Django web framework 4.1.4
- sqlite3
- Docker

## Why did I choose this stack?

I started out by having a general idea of the type of site that I wanted to make. I understood that I will need to have a CRUD based backend along with a database to manage the data. After researching various frameworks, I concluded that Django made the most sense. I wanted to stay within a Python based framework as that is the main language that I will be focusing on in my development work. SQLite comes with Django as the default dev database.

I also wwanted to learn more about Docker, which is why I decided to package my app into a container. This makes it very easu for me to share my dev environment with other devs, regardless of what type of system, packages and OS that they are running.

## What are the files and how does it work?

### Root directory

* buildbackend.sh - Script that builds the Docker container
* Dockerfile - Configuration file that Docker uses when building the container
* requirements.txt - List of additional packages that need to be installed in the container environment
* runbackend.sh - Script that runs the Docker container, which also mounts a file folder in the container (/app) with a local directory ($pwd/code). This ensures that files (including database) are not lost when the container shuts down

### code directory

* db.sqlite3 - Database
* manage.py - Default Django manage.py file used to manage various actions within the framework
* start.sh - Script to start the local dev webserver and expose it on localhost port 8080

### code/mysite - This is the Django project folder and I made changes to the following files:

* settings.py - Included my app 'displays' in the ``INSTALLED_APPS`` list. This way django knows about my app when it comes to things like making database migrations
* urls.py - Added a new path in the ``urlpatterns`` list. This routes all incoming requests (other than /admin) to my application, which then has its own urls.py file for different routes

### code/displays - This is the Django application folder for the website. My project only contains this single app. I made changes to the following files:

* apps.py - Added ``class DisplaysConfig`` so this way I can use the built in Django admin interface to view/edit my applications data in the database
* forms.py - Added ``class CreateDisplayForm(forms.ModelForm)`` - This is the main file to handle the management of a form for my data. Using ``ModelForm`` gave me a simple way to use the existing fields of my data model for the form, keeping in mind the DRY principle
* models.py - Added ``class Display(models.Model)`` - This is the data model that contains all of the fields for the database. It creates a single model/database object with the name 'Display'. Most of the fields are required, however some are set with ``blank=True``
* urls.py - There are 6 URL routes/patterns within the ``urlpatterns`` list. Whenever one of the routes are called by a browser, an associated function within views.py is then called. There are several different URLs to handle the various CRUD methods
* views.py - This is where most of the heavy lifting is done. It is also the file where I wrote most of my code. There are various functions that process the different CRUD operations. Since I used django templates to generate the HTML pages, I relied heavily on the ``render()`` function, which takes the data from the request, along with some additional context from form data and passes it to the template, where it can then be used as needed and output to HTML

### code/templates - These are the various Django template files. I create a main template called ``base.html``. All of the other templates extend that template. The templates rely on form data being passed to them from the view. I also used some basic conditionals and for loops, which are available within the django template syntax.

### code/static - Folder contains static files, such as styles.css and a JPG for the website logo

## How to run application

* Clone repo to your local machine
* Install Docker (If it is not already installed)
* Execute ``buildbackend.sh``
* Execute ``runbackend.sh``
* CD into the app folder
* Execute ``start.sh``
* Open browser and browse to http://localhost:8080/

## Future enhancements

* Do not display deleted displays in listings
* Ability to sort listings
* Ability to search/filter listings, including ability to search for displays that are X miles from Address/ZIP
* View listings on a map
* Return 404 if the details route is being requested for a display that is marked deleted
* User management/authentication
* Ability for users to only add/edit/delete their own listings
* Ability for user to create and manage lists, such as favorites, etc.
* Ability for file management, so users can upload photos of their displays and they can be shown on the display details page
* Ability to embded videos (YouTube/Vimeo) so they can be shown/played on the display details page
