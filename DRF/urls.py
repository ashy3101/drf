from django.urls import path
from DRF.views import home, create, listt, get, update, post, delete

urlpatterns=[
    path('', home, name="homepage"),

    path('create', create, name="create"),
    path('list/', listt.as_view(), name="GET request"), #view all database entries
    path('<username>/', get, name="GET request"),       #view particular database using username
    path('<username>/update', update, name="PUT"),      #update particular database fields
    path('post', post, name="POST"),                    #create new database
    path('<username>/delete', delete, name="delete"),   #delete the particular database


]