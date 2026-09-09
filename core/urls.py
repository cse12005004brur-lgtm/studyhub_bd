from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('notes/', views.notes_list_view, name='notes_list'),
    path('class/<str:class_name>/', views.class_notes_view, name='class_notes'),
    path('register/', views.register_view, name='register'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path(
        'favorite/<int:note_id>/',
        views.toggle_favorite,
        name='toggle_favorite',
    ),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/add/', views.add_note_view, name='add_note'),
    path(
        'admin-dashboard/edit/<int:note_id>/',
        views.edit_note_view,
        name='edit_note',
    ),
    path(
        'admin-dashboard/delete/<int:note_id>/',
        views.delete_note_view,
        name='delete_note',
    ),
]