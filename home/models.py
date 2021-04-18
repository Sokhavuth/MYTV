import shortuuid
from django.db import models

class Movie(models.Model):
    movie_id = models.CharField(max_length=255, editable=False, default=shortuuid.uuid())
    movie_title = models.CharField(max_length=255)
    video_type = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255)
    post_content = models.TextField()
    country_origin = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    publisher = models.CharField(max_length=255)
