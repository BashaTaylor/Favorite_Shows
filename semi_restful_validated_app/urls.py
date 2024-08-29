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
