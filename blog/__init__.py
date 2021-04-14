#new app by named blog->py manage.py startapp blog.
# in views.py of new app 

#this is from views.py
#home function if to mange the trafic users see this when sent to the route.
#to pass html using templates we create a template directory.
#then cret a new dir names same as the app ie> in this case blog inside the templates and add the 
#.html file there. here 2 are added home.html and about.html
#the add the class name in the app.py to list of installed apps in settings.py
#template inheritance for conbinnig all repeated code at one place
#in django static folder needs to be located in a directory called static and inthat a new folder with the same name as the app
#same as the templates directory so static->blog
#then in the base.html {% load static %} then there is a link tag added at line 13
#added href="{% static 'blog/main.css' %}" here static creates a absolute reference to the static directory