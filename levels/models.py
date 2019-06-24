from mongoengine import DynamicDocument
from mongoengine.fields import (
    StringField, IntField, DictField,
    DateTimeField, ObjectId, FloatField,
    BooleanField
)
 
class PowerModel(DynamicDocument):
    username = StringField()
    host = StringField()
    blockchain = StringField()
    power = IntField()
    staked = IntField()
    delegated = IntField()
    
    meta = {
        'collection': 'powers',
        'ordering': ['-date'],

        'indexes': [
            'username',
            'host',
            'blockchain',
            'power',
        ],

        'auto_create_index': True,
        'index_background': True
    }



class HostModel(DynamicDocument):
    username = StringField()
    levels = DictField()
    blockchain = StringField()
    registered_at = DateTimeField()
    architect = StringField()
    hoperator = StringField()
    consensus_percent = FloatField()
    referral_percent = FloatField()
    dac_mode = IntField()
    dacs = DictField()
    chosts = DictField()
    ahost = StringField()
    non_active_chost = BooleanField()
    need_switch = BooleanField()
    fhosts_mode = IntField()
    fhosts = DictField()
    title = StringField()
    purpose = StringField()
    total_shares = IntField()
    quote_amount = StringField()
    root_token_contract = StringField()
    root_token = StringField()
    symbol = StringField()
    precision = IntField()
    to_pay = IntField()
    payed = BooleanField()
    cycle_start_id = IntField()
    current_pool_id = IntField()
    current_cycle_num = IntField()
    current_pool_num = IntField()
    parameters_setted = BooleanField()
    activated = BooleanField()
    priority_flag = BooleanField()
    meta = StringField()
    app = StringField()


    meta = {
        'collection': 'hosts',
        'ordering': ['-registered_at'],

        'indexes': [
            'username',
            'blockchain',
            'ahost',
            'activated',
            'payed',
            'parameters_setted'
            'priority_flag'
            'need_switch',
            'non_active_chost',
            'app'
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
