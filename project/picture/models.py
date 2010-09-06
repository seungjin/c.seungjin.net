# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AccessLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    timezone = models.CharField(max_length=120, blank=True)
    remote_ip = models.CharField(max_length=120, blank=True)
    user_agent = models.TextField(blank=True)
    url = models.CharField(max_length=768, blank=True)
    http_referer = models.CharField(max_length=768, blank=True)
    class Meta:
        db_table = u'access_logs'

class Pictures(models.Model):
    id = models.IntegerField(primary_key=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=768, blank=True)
    file_name = models.CharField(max_length=768, blank=True)
    content_type = models.TextField(blank=True)
    image_blob = models.TextField(blank=True)
    publishing_code = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'pictures'

