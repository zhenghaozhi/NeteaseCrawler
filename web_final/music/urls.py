from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('home/', views.home, name='home'),
    
    path('song_list/', views.song_list, name='song_list'),
    path('artist_list/', views.artist_list, name='artist_list'),

    path('song/<int:music_id_in>/', views.song_detail, name='song_detail'),
    path('artist/<int:artist_id_in>/', views.artist_detail, name='artist_detail'),

    path('search/', views.search, name='search'),
    path('search_artists/results/', views.search_artists, name='search_artists'),
    path('search_songs/results/', views.search_songs, name='search_songs'),
    
    path('music/<int:music_id_in>/add_comment/', views.add_comment, name='add_comment'),
    path('music/<int:music_id_in>/delete_comment/<comment_id>/', views.delete_comment, name='delete_comment'),
]
