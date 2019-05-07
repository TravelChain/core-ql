from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DictField,
    DateTimeField, ObjectId, FloatField,
    BooleanField
)
 
class BadgeTypeModel(DynamicDocument):
    host = StringField()
    ownid = IntField()
    blockchain = StringField()
    caption = StringField()
    iurl = StringField()
    description = StringField()
    power = IntField()
    total = IntField()
    remain = IntField()

    meta = {
        'collection': 'badgetypes',
        'ordering': ['-date'],

        'indexes': [
            'ownid',
            'host',
            'blockchain',
        ],

        'auto_create_index': True,
        'index_background': True
    }

class BadgeModel(DynamicDocument):
    username = StringField()
    host = StringField()
    blockchain = StringField()
    badgetype = StringField()
    comment = StringField()
    backed = BooleanField()
    backreason = StringField()

    meta = {
        'collection': 'badges',
        'ordering': ['-date'],

        'indexes': [
            'username',
            'host',
            'blockchain',
            'badgetype',
        ],

        'auto_create_index': True,
        'index_background': True
    }

