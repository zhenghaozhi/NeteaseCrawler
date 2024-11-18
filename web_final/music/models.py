from django.db import models

# Create your models here.

class music(models.Model):
    class Meta:
        db_table = 'music'
    id = models.IntegerField(primary_key=True)
    url = models.TextField()
    music_name = models.TextField()
    sub_music_name = models.TextField(blank=True, null=True)
    album_name = models.TextField(blank=True, null=True)
    album_id = models.TextField(blank=True, null=True)
    artist_name = models.TextField()
    artist_id = models.TextField()
    sub_artist_name = models.TextField(blank=True, null=True)
    sub_artist_id = models.TextField(blank=True, null=True)
    artist_cnt = models.IntegerField(default=0)
    lyrics = models.TextField(blank=True, null=True)
    lyrics_pure = models.TextField(blank=True, null=True)
    translated_lyrics_pure = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)

    # artist = models.ManyToManyField('artist', through='relations')

class artist(models.Model):
    class Meta:
        db_table = 'artist'
    id = models.IntegerField(primary_key=True)
    url = models.TextField()
    artist_name = models.TextField()
    sub_artist_name = models.TextField(blank=True, null=True)
    artist_info = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)

class relations(models.Model):
    class Meta:
        db_table = 'relations'
        # unique_together = (('music', 'artist'),)
    id = models.IntegerField(primary_key=True)
    music = models.ForeignKey(music, on_delete=models.CASCADE)
    artist = models.ForeignKey(artist, on_delete=models.CASCADE)
