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

class DailyPhotoStream(models.Model):
    id = models.IntegerField(primary_key=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=768, blank=True)
    photo_path = models.CharField(max_length=768, blank=True)
    photo_blob = models.TextField(blank=True)
    photo_thumbnail_path = models.CharField(max_length=768, blank=True)
    photo_thunbnail_blob = models.TextField(blank=True)
    class Meta:
        db_table = u'daily_photo_stream'

class EmailReceived(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=21)
    from_field = models.CharField(max_length=768, db_column='from', blank=True) # Field renamed because it was a Python reserved word. Field name made lowercase.
    to = models.CharField(max_length=768, blank=True)
    subject = models.CharField(max_length=768, blank=True)
    body = models.TextField(blank=True)
    rfc822 = models.TextField(blank=True)
    received_at = models.CharField(max_length=768, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'email_received'

class Guestbooks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=768, blank=True)
    timestamp = models.CharField(max_length=72, blank=True)
    timezone = models.CharField(max_length=33, blank=True)
    message = models.TextField(blank=True)
    publishing_code = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=768, blank=True)
    remote_ip = models.CharField(max_length=33, blank=True)
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'guestbooks'

class Hosts(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=45, blank=True)
    hostname = models.CharField(max_length=768, blank=True)
    type = models.CharField(max_length=42, blank=True)
    username = models.CharField(max_length=768, blank=True)
    password = models.CharField(max_length=768, blank=True)
    id_rsa_pub = models.TextField(blank=True)
    service_provider = models.CharField(max_length=768, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'hosts'

class IdRsaPub(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=765, blank=True)
    key = models.TextField(blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'id_rsa_pub'

class Journals(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.CharField(max_length=33, blank=True)
    time = models.CharField(max_length=33, blank=True)
    timezone = models.CharField(max_length=768, blank=True)
    tag = models.CharField(max_length=768, blank=True)
    subject = models.TextField(blank=True)
    publishing_code = models.IntegerField(null=True, blank=True)
    body = models.TextField(blank=True)
    ref = models.CharField(max_length=768, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'journals'

class MyGeoips(models.Model):
    id = models.IntegerField(primary_key=True)
    remote_ip = models.CharField(max_length=120, blank=True)
    geo = models.TextField(blank=True)
    note = models.CharField(max_length=768, blank=True)
    timestamp = models.DateTimeField()
    timezone = models.CharField(max_length=120, blank=True)
    referring_access_logs_id = models.IntegerField()
    class Meta:
        db_table = u'my_geoips'

class Tmp(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.TextField(blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tmp'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=765)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField()
    class Meta:
        db_table = u'users'

