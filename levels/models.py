from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DictField,
    DateTimeField, ObjectId, FloatField,
    BooleanField
)
 
class HostModel(DynamicDocument):
    username = StringField()
    levels = DictField()
    blockchain = StringField()
    meta = {
        'collection': 'hosts',
        'ordering': ['-date'],

        'indexes': [
            'username',
            'levels',
            'blockchain',
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
    blockchain = StringField()

    meta = {
        'collection': 'balances',
        'ordering': ['-date'],

        'indexes': [
            'blockchain',
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
    blockchain = StringField()
    username = StringField()
    referer = StringField()
    meta = StringField()
    meta = {
        'collection': 'users',
        'ordering': ['-date'],

        'indexes': [
            'blockchain',
            'username',
            'referer',
        ],

        'auto_create_index': True,
        'index_background': True
    }
