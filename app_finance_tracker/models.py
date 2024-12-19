from django.db import models

class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    user = models.TextField(max_length=80)
    table_name = models.TextField(max_length=80)

class Tracker(models.Model):
    table_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    date = models.DateField()
    type = models.TextField()
    category = models.TextField()
    description = models.TextField()
    amount = models.IntegerField()