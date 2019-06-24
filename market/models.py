from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DictField,
    DateTimeField, ObjectId, FloatField,
    BooleanField
)

class SpiralModel(DynamicDocument):
    blockchain = StringField()
    host = StringField()
    ahost = StringField()
    size_of_pool = IntField()
    overlap = IntField()
    profit_growth = IntField()
    base_rate = IntField()
    loss_percent = IntField()
    pool_limit = IntField()
    pool_timeout = IntField()
    priority_seconds = IntField()

    meta = {
        'collection': 'spirals',
        'ordering': ['_id'],

        'indexes': [
            'blockchain',
            'host',
            'ahost',
            
        ],

        'auto_create_index': True,
        'index_background': True
    }
  


class SpiralModel(DynamicDocument):
    blockchain = StringField()
    host = StringField()
    ahost = StringField()
    size_of_pool = IntField()
    overlap = IntField()
    profit_growth = IntField()
    base_rate = IntField()
    loss_percent = IntField()
    pool_limit = IntField()
    pool_timeout = IntField()
    priority_seconds = IntField()
      
    meta = {
        'collection': 'spirals',
        'ordering': ['_id'],

        'indexes': [
            'blockchain',
            'host',
            'ahost',
            
        ],

        'auto_create_index': True,
        'index_background': True
    }


class RatesModel(DynamicDocument):
    blockchain = StringField()
    pool_id = IntField()
    host = StringField()
    ahost = StringField()
    total_quants = IntField()
    buy_rate = IntField()
    sell_rate = IntField()
    client_income = StringField()
    delta = StringField()
    pool_cost = StringField()
    total_in_box = StringField()
    payment_to_wins = StringField()
    payment_to_loss = StringField()
    system_income = StringField()
    live_balance_for_sale = StringField()

    meta = {
        'collection': 'rates',
        'ordering': ['_id'],

        'indexes': [
            'blockchain',
            'host',
            'ahost',
            'pool_id'
            
        ],

        'auto_create_index': True,
        'index_background': True
    }
  

class CoreMarketModel(DynamicDocument):
    blockchain = StringField()
    host = StringField()
    pool_id = IntField()
    pool_num = IntField()
    cycle_num = IntField()
    color = StringField()
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    type = StringField()
    timestamp = DateTimeField()
    
    meta = {
        'collection': 'coremarkets',
        'ordering': ['-cycle_num'],

        'indexes': [
            'blockchain',
            'host',
            'timestamp',
            'type',
            'cycle_num'
    
        ],

        'auto_create_index': True,
        'index_background': True
    }
  
class MarketModel(DynamicDocument):
    blockchain = StringField()
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
            'blockchain',
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
