import shortuuid
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
  CHOICES = (
        ('YT', 'YouTube'),
        ('FB', 'Facebook'),
        ('OK', 'Одноклассники'),
        ('DM', 'Dailymotion'),
        ('VM', 'Vimeo'),
    )

  movie_id = models.CharField(max_length=255, editable=False, default=shortuuid.uuid())
  movie_title = models.CharField(max_length=255)
  video_type = models.CharField(max_length=255, choices = CHOICES, default=1)
  video_id = models.CharField(max_length=255)
  post_content = models.TextField(blank=True)
  country_origin = models.CharField(max_length=255)
  pub_date = models.DateTimeField('date published')
  published_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
