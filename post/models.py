from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DictField,
    DateTimeField, ObjectId, FloatField,
    BooleanField
)
   

class VoteModel(DynamicDocument):
    author = StringField()
    voter = StringField()
    comment = ObjectId()
    last_update = DateTimeField()
    num_changes = IntField()
    permlink = StringField()
    rshares = IntField()
    vote_percent = IntField()
    weight = FloatField()

    meta = {
        'collection': 'comment_vote_object',
        'indexes': [
            'author',
            'voter',
            'comment',
            'permlink',
            'parent_permlink',
            'last_update'
        ],

        'auto_create_index': True,
        'index_background': True
    }


class CommentModel(DynamicDocument):   
    blockchain = StringField()
    author = StringField()
    parent_author = StringField()
    created = DateTimeField()
    last_update = DateTimeField()
    permlink = StringField()
    parent_permlink = StringField()
    body = StringField()
    title = StringField()
    meta = StringField()
    
    json = DictField()

    meta = {
        'collection': 'posts',
        'ordering': ['-created'],

        'indexes': [
            'blockchain',
            'author',
            'parent_author',
            'permlink',
            'parent_permlink',
            'created',
            'json.app',
            'json.tags'
        ],

        'auto_create_index': True,
        'index_background': True
    }
