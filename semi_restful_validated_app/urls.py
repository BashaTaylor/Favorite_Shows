from django.urls import path
from .import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Display all shows
    path('shows', views.index, name='all_shows'),  # Optional: a route for listing all shows
    path('shows/new', views.new, name='new'),  # Display form to create a new show
    path('shows/create', views.create, name='create'),  # Handle show creation

    path('shows/<int:show_id>/show', views.show, name='show'),  # Display specific show details
    path('shows/<int:show_id>/edit', views.edit, name='edit'),  # Edit a specific show
    path('shows/<int:show_id>/update', views.update, name='update'),  # Update a specific show
    path('shows/<int:show_id>/delete', views.delete, name='delete'),  # Delete a specific show
]


# urlpatterns = [
#     path('', views.index), #GET request redirecting to shows route
#     path('show', views.show), #GET request to display all objects' info starting at a different root
#     path('show/new', views.new), #GET request to display form to create an object ( a new show)
#     path('show/create', views.create), #POST request to create an object

#     path('shows/<int:show_id>/show', views.show), #GET request to display a specific object's info
#     path('shows/<int:show_id>/edit', views.edit), #GET request to display form to update a specific object
#     path('shows/<int:show_id>/update', views.update), #POST request to update a specific object
#     path('shows/<int:show_id>/delete', views.delete), #POST request to delete a specific object
# ]