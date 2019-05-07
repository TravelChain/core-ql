from contextlib import suppress

from mongoengine.base.datastructures import BaseDict
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene.types.generic import GenericScalar
from common.utils import find_users, count_users
from levels.models import (
    LevelModel, BalanceModel, HostModel, PowerModel, 
)
from badges.models import (BadgeModel)
from common.utils import prepare_json
from common.types import GeometryObjectType
from common.fields import CustomMongoengineConnectionField
from pprint import pprint


class Power(MongoengineObjectType):
    # powers = graphene.List('levels.types.Power',
    #                          blockchain=graphene.String(required=True),
    #                          host = graphene.String(required=True),
    #                          first=graphene.Int(),
    #                          last=graphene.Int())
    
    # def resolve_powers(self, info, blockchain, host):
        
    #     qs = PowerModel.objects(blockchain=blockchain, username = self.username, host=host)
    #     return qs;
    badges = graphene.List('badges.types.Badge', first=graphene.Int(),
                             last=graphene.Int(),   
                             )

    json_metadata = GenericScalar()

    avatar = graphene.String()


    def resolve_avatar(self, info):
        user = LevelModel.objects(username=self.username, blockchain = self.blockchain).first()
        meta = prepare_json(user.meta)
        
        if 'img' in meta:
            print("1")
            return meta['img']
        else:
            print("2")
            return "/ava.png"    


    def resolve_json_metadata(self, info):
        User = LevelModel.objects(username = self.username, blockchain = self.blockchain).first()
        
        return prepare_json(User.meta)

        # if isinstance(self.meta, BaseDict):
        #     return prepare_json(self.meta)
        # else: 
        #     return {}
    

    def resolve_badges(self, info):
        
        qs = BadgeModel.objects(blockchain = self.blockchain, username = self.username)
        #TODO find badges and construct
        return qs;

    class Meta:
        model = PowerModel
        interfaces = (Node, )


    
    

class Balance(MongoengineObjectType):



    class Meta:
        model = BalanceModel
        interfaces = (Node, )


class Host(MongoengineObjectType):

    class Meta:
        model= HostModel
        interfaces = (Node, )

class Level(MongoengineObjectType):

    levels = graphene.List('levels.types.Level',
                             blockchain=graphene.String(required=True),
                             first=graphene.Int(),
                             last=graphene.Int())

    balances = graphene.List('levels.types.Balance',
                             blockchain=graphene.String(required=True),
                             host = graphene.String(required=True))

    powers = graphene.List('levels.types.Power',
                             blockchain=graphene.String(required=True),
                             host = graphene.String(required=True),
                             first=graphene.Int(),
                             last=graphene.Int())

    badges = graphene.List('badges.types.Badge', first=graphene.Int(),
                             last=graphene.Int(),   
                             )


    exp_summ_black = graphene.Float(blockchain=graphene.String(required=True),host=graphene.String(required=True), level = graphene.Int(required=True))
    exp_summ_white = graphene.Float(blockchain=graphene.String(required=True),host=graphene.String(required=True), level = graphene.Int(required=True))

    total_recieved = graphene.Float(blockchain=graphene.String(required=True),host=graphene.String(required=True), level = graphene.Int(required=True))
    
    info = GenericScalar()
    avatar = graphene.String()
    count = graphene.Int()

    gdp = graphene.Float()
    
    nickname = graphene.String()

    def resolve_nickname(self, info):
        user = LevelModel.objects(username=self.username, blockchain = self.blockchain).first()
        meta = prepare_json(user.meta)
        
        if 'nickname' in meta:
            return meta['nickname']
        else:
            return ""   


    # rec_summ_black = graphene.Float(host=graphene.String(), level = graphene.Int())
    # rec_summ_white = graphene.Float(host=graphene.String(), level = graphene.Int())

    # def resolve_gdp(self, info, host):
    
    def resolve_badges(self, info):
        
        qs = BadgeModel.objects(blockchain = self.blockchain, username = self.username)
        #TODO find badges and construct
        return qs;


    def resolve_powers(self, info, blockchain, host):
        qs = PowerModel.objects(blockchain=blockchain, username = self.username, host=host)
        return qs;

    def resolve_count(self, info):
        return 1
        
    def resolve_info(self, info):
        # if isinstance(self.meta, BaseDict):
        return prepare_json(self.meta)
        # else: 
            # return {}

    def resolve_avatar(self, info):
        info = prepare_json(self.meta)
        if 'img' in info:
            return info['img']
        else:
            return ""

    def resolve_exp_summ_black(self, info, blockchain, host, level):
        print("blockchain: ", self.blockchain)

        balance = BalanceModel.objects(username = self.username, blockchain=blockchain, host = host, pool_color = "black", withdrawed = False)
        summ = 0
        host = HostModel.objects(username = host)
        lev = host[0]['levels'][level - 1]
        
        for bal in balance:
            spl = bal.ref_amount.split(" ")
            summ = summ + float(spl[0]) * lev / 1000000
            summ = round(summ,8);

        return summ

    def resolve_exp_summ_white(self, info, blockchain, host, level):
        print("blockchain:", self.blockchain)
        balance = BalanceModel.objects(username = self.username, blockchain = blockchain, host = host, pool_color = "white", withdrawed = False)
        summ = 0
        host = HostModel.objects(username = host)
        lev = host[0]['levels'][level - 1]

        for bal in balance:
            spl = bal.ref_amount.split(" ")
            summ = summ + float(spl[0]) * lev / 1000000
            summ = round(summ,8);
            print(summ)
        return summ
    

    def resolve_total_recieved(self, info, blockchain, host, level):
        print("username", self.username)
        print("blockchain", blockchain)
        print('host', host)

        balance = BalanceModel.objects(username = self.username, blockchain = blockchain, host = host, win = True, withdrawed = True)
        print(balance)
        summ = 0
        host = HostModel.objects(username = host)
        lev = host[0]['levels'][level - 1]

        for bal in balance:
            spl = bal.ref_amount.split(" ")
            summ = summ + float(spl[0]) * lev / 1000000
            summ = round(summ,8);
            print(summ)
        return summ


    # def resolve_lev(self, info, first=None, last=None):
    #     # print(self.username)
    #     # print(parent)
    #     # lev = get_level(self)
    #     if hasattr(self, 'lev'):
    #         return self.lev + 1
    #     else:
    #         return 1

    # level = CustomMongoengineConnectionField(Level)

    def resolve_levels(self, info, blockchain, first=None, last=None):
        # TODO Написать простой пагинатор для комментов
        username = find_users(self, blockchain)

        return username
    
    def resolve_balances(self, info, host):

        balance = BalanceModel.objects(username = self.username, host  = host)
        # for i, bal in enumerate(balance):
        #     print(i)
        #     spl = bal.ref_amount.split(" ")
        #     balance[i] = float(spl[0])

        return balance
    
    

    class Meta:
        model = LevelModel
        interfaces = (Node, )

    