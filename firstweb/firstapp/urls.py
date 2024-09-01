from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('admin/', admin.site.urls),
    path('about_us/', views.about_us, name='about_us'),
    path('autorization/', views.autorization, name='autorization'),
    path('main_page/', views.main_page, name='main_page'),
    path('registrationPlayers/', views.registrationPlayers, name='registrationPlayers'),
    path('edit_player/<int:player_id>/', views.edit_player, name='edit_player'),
    path('delete_player/<int:player_id>/', views.delete_player, name='delete_player'),
    path('SortPlayers/', views.select_players, name='SortPlayers'),
    path('sort_players/', views.sort_players, name='sort_players'),
    path('edit_coefficient/<int:id>/', views.edit_coefficient, name='edit_coefficient'),
    path('history/', views.match_history, name='history'),
]
