# from django.shortcuts import render

# Create your views here.

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import music, artist, relations
from django.utils import timezone

from django.db.models import Q
import time
import json

def song_list(request): 
    print("# Requesting song lists...")
    song_list = music.objects.all()
    paginator = Paginator(song_list, 30)   # 30 each time

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'music/song_list.html', {'page_obj': page_obj})

def artist_list(request):
    artist_list = artist.objects.all()
    paginator = Paginator(artist_list, 20)   # 20 each time

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'music/artist_list.html', {'page_obj': page_obj})

def song_detail(request, music_id_in):
    print("# Requesting songs...")
    song = get_object_or_404(music, id=music_id_in)
    art = get_object_or_404(artist, artist_name=song.artist_name)
    sub_art = artist.objects.filter(artist_name=song.sub_artist_name).first()
    print("| Requested.")
    comments = json.loads(song.comment) if song.comment else []
    comments = sorted(comments, key=lambda x: x['time'], reverse=True)
    song.artist_cnt = int(song.artist_cnt)

    lyrics_json_str = song.lyrics
    lyrics_dict = json.loads(lyrics_json_str)
    lyrics_list = list(lyrics_dict.values())

    return render(request, 'music/song_detail.html', {
        'song': song,
        'artist': art,
        'sub_artist': sub_art,
        'comments': comments,
        'lyrics_list': lyrics_list
    })



def add_comment(request, music_id_in):
    if request.method == 'POST':
        song = get_object_or_404(music, id=music_id_in)
        new_comment = {
            'username': request.POST['username'],
            'text': request.POST['comment_text'],
            'time': timezone.localtime().strftime('%Y-%m-%d %H:%M:%S'),
            'id': str(timezone.now().timestamp())  # unique
        }
        comments = json.loads(song.comment) if song.comment else []
        comments.append(new_comment)
        song.comment = json.dumps(comments)
        song.save()
    return redirect('song_detail', music_id_in=music_id_in)

def delete_comment(request, music_id_in, comment_id):
    if request.method == 'POST':
        song = get_object_or_404(music, id=music_id_in)
        comments = json.loads(song.comment) if song.comment else []
        comments = [comment for comment in comments if comment['id'] != comment_id]
        song.comment = json.dumps(comments)
        song.save()
    return redirect('song_detail', music_id_in=music_id_in)

def artist_detail(request, artist_id_in):
    print("# Requesting artists...")

    artists = artist.objects.get(id=artist_id_in)
    relation = relations.objects.filter(artist=artists)
    songs = [rel.music for rel in relation]

    print("| Requested.")
    return render(request, 'music/artist_detail.html', {'artist': artists, 'song': songs})

def search(request):
    return render(request, 'music/search.html')

def search_songs(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    print("# Searching...")
    start_time = time.time()
    
    if search_type == 'song':
        full_matches = music.objects.filter(Q(music_name__iexact=query) | Q(artist_name__iexact=query) | Q(sub_artist_name__iexact=query) | Q(lyrics_pure__iexact=query) | Q(translated_lyrics_pure__iexact=query))
        partial_matches = music.objects.filter(Q(music_name__icontains=query) | Q(artist_name__icontains=query) | Q(sub_artist_name__icontains=query) | Q(lyrics_pure__icontains=query) | Q(translated_lyrics_pure__icontains=query)).exclude(id__in=[song.id for song in full_matches])
    else:  # 'artist'
        song_matches = music.objects.filter(Q(music_name__iexact=query)).values_list('artist_name', flat=True)
        sub_song_matches = music.objects.filter(Q(music_name__iexact=query)).values_list('sub_artist_name', flat=True)
        if (len(song_matches)):
            full_matches = artist.objects.filter(Q(artist_name__iexact=query) | Q(artist_info__iexact=query) | Q(artist_name__iexact=str(song_matches[0])) | Q(artist_name__iexact=str(sub_song_matches[0])))
        else:
            full_matches = artist.objects.filter(Q(artist_name__iexact=query) | Q(artist_info__iexact=query))
        partial_matches = artist.objects.filter(Q(artist_name__icontains=query) | Q(artist_info__icontains=query)).exclude(id__in=[artist.id for artist in full_matches])
    
    end_time = time.time()
    search_time = end_time - start_time
    print("| Search completed in " + str(search_time) + "s")
    
    paginator = Paginator(partial_matches, 20)   # 20 each time

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'search_type': search_type,
        'full_matches': full_matches,
        'partial_matches': page_obj,
        'search_time': search_time,
        'total_results': full_matches.count() + partial_matches.count(),
        'page_obj': page_obj
    }
    return render(request, 'music/search_songs.html', context)

def search_artists(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    print("# Searching...")
    start_time = time.time()
    
    if search_type == 'song':
        full_matches = music.objects.filter(Q(music_name__iexact=query) | Q(artist_name__iexact=query) | Q(sub_artist_name__iexact=query) | Q(lyrics_pure__iexact=query) | Q(translated_lyrics_pure__iexact=query))
        partial_matches = music.objects.filter(Q(music_name__icontains=query) | Q(artist_name__icontains=query) | Q(sub_artist_name__icontains=query) | Q(lyrics_pure__icontains=query) | Q(translated_lyrics_pure__icontains=query)).exclude(id__in=[song.id for song in full_matches])
    else:  # 'artist'
        song_matches = music.objects.filter(Q(music_name__iexact=query)).values_list('artist_name', flat=True)
        sub_song_matches = music.objects.filter(Q(music_name__iexact=query)).values_list('sub_artist_name', flat=True)
        if (len(song_matches)):
            full_matches = artist.objects.filter(Q(artist_name__iexact=query) | Q(artist_info__iexact=query) | Q(artist_name__iexact=str(song_matches[0])) | Q(artist_name__iexact=str(sub_song_matches[0])))
        else:
            full_matches = artist.objects.filter(Q(artist_name__iexact=query) | Q(artist_info__iexact=query))
        partial_matches = artist.objects.filter(Q(artist_name__icontains=query) | Q(artist_info__icontains=query)).exclude(id__in=[artist.id for artist in full_matches])
    
    end_time = time.time()
    search_time = end_time - start_time
    print("| Search completed in " + str(search_time) + "s")
    
    paginator = Paginator(partial_matches, 20)   # 20 each time

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'search_type': search_type,
        'full_matches': full_matches,
        'partial_matches': page_obj,
        'search_time': search_time,
        'total_results': full_matches.count() + partial_matches.count(),
        'page_obj': page_obj
    }
    return render(request, 'music/search_artists.html', context)

def home(request):
    return render(request, 'music/home.html')