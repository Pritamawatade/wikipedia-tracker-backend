from django.db import models

class ReadingProgress(models.Model):
    user_id = models.CharField(max_length=255)  # User identifier
    article_url = models.URLField()            # Wikipedia article URL
    progress_percentage = models.FloatField()  # Reading progress
    updated_at = models.DateTimeField(auto_now=True)  # Last updated time

