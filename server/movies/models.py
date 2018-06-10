from django.db import models

# Create your models here.


from mongoengine import Document, fields

class Movie(Document):
    mvid = fields.IntField(required=True,min_value=0)
    title = fields.DictField(required=True)
    poster=fields.DynamicField(required=True)
    rtscore = fields.IntField(required=True,min_value=0,max_value=100)
    audscore = fields.IntField(required=True,min_value=0,max_value=100)
    nnoscars = fields.IntField(required=True,min_value=0)
    nwoscars = fields.IntField(required=True,min_value=0)
    nnglobes = fields.IntField(required=True,min_value=0)
    nwglobes = fields.IntField(required=True,min_value=0)
    date = fields.IntField(required=True,min_value=0)
    duration = fields.IntField(required=True,min_value=0)
    resolution = fields.StringField(default=None, blank=True, null=True)
    hd = fields.StringField(default=None, blank=True, null=True)
    trailer = fields.DictField(default=None)
    catchy=fields.DictField(required=True)
    description = fields.DictField(required=True)
    genres=fields.DictField(required=True)
    useTMDB = fields.BooleanField(required=True)
    tmdbID=fields.StringField()
    imdbID=fields.StringField()



