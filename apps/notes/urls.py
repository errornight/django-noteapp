from django.urls import path, include
from . import views
from apps.users import views as user_view

urlpatterns = [
    path('', views.home, name='HomePage'),
    path('about-us/', user_view.about_us, name='About-usPage'),

    path('notes/', views.notes_page, name='NotesPage'),
    path('notes/add', views.add_note, name='AddNote'),
    path('notes/edit/<str:username>/<uuid:uuid>/', views.edit_note, name='EditNotePage'),
    path('notes/delete/<str:username>/<uuid:uuid>/', views.delete_note, name='DeleteNote'),
    path('notes/<str:username>/<uuid:uuid>/', views.note_page, name='NotePage'),

]

