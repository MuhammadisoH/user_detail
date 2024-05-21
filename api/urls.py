from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.get_notes),                        # localhost:8000/api/notes/
    path('notes/new/', views.create_note),                  # localhost:8000/api/notes/new
    path('notes/<uuid:id>/', views.note_detail),            # localhost:8000/api/notes/:id

    path('users/', views.get_users),                        # localhost:8000/api/users/
    path('users/new/', views.create_user),                  # localhost:8000/api/notes/new
    path('users/<int:id>/', views.user_detail),             # localhost:8000/api/users/:id
]
