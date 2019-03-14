from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DictField,
    DateTimeField, ObjectId, FloatField,
    BooleanField
)
 
class HostModel(DynamicDocument):
    username = StringField()
    levels = DictField()

    meta = {
        'collection': 'hosts',
        'ordering': ['-date'],

        'indexes': [
            'username',
            'levels',
        ],

        'auto_create_index': True,
        'index_background': True
    }

class BalanceModel(DynamicDocument):
    ref_amount = StringField()
    win = BooleanField()
    host = StringField()
    pool_color = StringField()
    withdrawed = BooleanField()
    meta = {
        'collection': 'balances',
        'ordering': ['-date'],

        'indexes': [
            'ref_amount',
            'win',
            'host',
            'pool_color',
            'withdrawed'

        ],

        'auto_create_index': True,
        'index_background': True
    }

class LevelModel(DynamicDocument):
    username = StringField()
    referer = StringField()
    meta = StringField()
    meta = {
        'collection': 'users',
        'ordering': ['-date'],

        'indexes': [
            'username',
            'referer',
        ],

        'auto_create_index': True,
        'index_background': True
    }
