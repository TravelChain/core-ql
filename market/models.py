from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DictField,
    DateTimeField, ObjectId, FloatField,
    BooleanField
)
  
class MarketModel(DynamicDocument):
    host = StringField()
    date = DateTimeField()
    base = FloatField()
    quote = FloatField()
    basecurr = StringField()
    quotecurr = StringField()
    cost = FloatField()
    is1min = BooleanField()
    is5min = BooleanField()
    is15min = BooleanField()
    is30min = BooleanField()
    is60min = BooleanField()
    is4hour = BooleanField()
    is1day =  BooleanField()
    is1week = BooleanField()
    
    meta = {
        'collection': 'markets',
        'ordering': ['-date'],

        'indexes': [
            'host',
            'date',
            'is1min',
            'is5min',
            'is15min',
            'is30min',
            'is60min',
            'is4hour',
            'is1day', 
            'is1week'
    
        ],

        'auto_create_index': True,
        'index_background': True
    }
