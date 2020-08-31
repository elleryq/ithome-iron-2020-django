from django.db import models


# news/models.py
class Reporter(models.Model):
    name = models.CharField(max_length=250)


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
