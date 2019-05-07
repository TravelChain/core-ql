from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DateTimeField, BooleanField,
    FloatField, ListField, DictField
)



class AccountModel(DynamicDocument):
    username = StringField()
    blockchainn = StringField()
    referer = StringField()
    meta = StringField()


    meta = {
        'collection': 'users',
        'indexes': [
            'username',
            'referer',
            'blockchain'
        ],

        'auto_create_index': True,
        'index_background': True
    }
