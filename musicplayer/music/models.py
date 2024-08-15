from django.db import models

# Create your models here.
    
class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    song_name=models.CharField(max_length=200)
    singer=models.CharField(max_length=100)
    song_type=models.CharField(max_length=50)
    song=models.FileField(upload_to="documents")
    image=models.FileField(upload_to="documents")
    
    def __str__(self):
        return self.song_name


