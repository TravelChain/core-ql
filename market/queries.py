import graphene

from market.types import (Market, CoreMarket, Rates, Spiral)
from market.models import (MarketModel, CoreMarketModel, RatesModel, SpiralModel)
from common.fields import CustomMongoengineConnectionField
from pprint import pprint
from inspect import getmembers

class SpiralQuery(graphene.ObjectType):
    spiral = CustomMongoengineConnectionField(Spiral)

    def resolve_spiral(self, info, args):
        qs = SpiralModel.objects()
        return qs
        

class RatesQuery(graphene.ObjectType):
    rates = CustomMongoengineConnectionField(Rates)

    def resolve_rates(self, info, args):
        qs = RatesModel.objects()
        return qs

class CoreMarketQuery(graphene.ObjectType):
    coremarket = graphene.Field(CoreMarket, host=graphene.String(), cycleNum=graphene.Int())
    coremarkets = CustomMongoengineConnectionField(CoreMarket)
    lastcoremarkets = CustomMongoengineConnectionField(CoreMarket)

    # totalincome = graphene.Float()
    # incomeperround = graphene.Float()
    # risk = graphene.Float()

    # def resolve_totalincome(self, info, host):


    def resolve_coremarket(self, info, host, cycleNum):
        return CoreMarketModel.objects(host=host, cycleNum=cycleNum).first()

    def resolve_coremarkets(self, info, args):
        qs = CoreMarketModel.objects()
        return qs;

    def resolve_lastcoremarkets(self, info, args):
        host = args.get('host', 'none')
        last = CoreMarketModel.objects(host=host).first()
        if (last):
            qs = CoreMarketModel.objects(cycle_num = last.cycle_num)
            return qs;
        else:
            return [];


class MarketQuery(graphene.ObjectType):
    market = graphene.Field(Market, host=graphene.String())
    markets = CustomMongoengineConnectionField(Market)

    # def resolve_accounts(self, info, args):
    #     qs = AccountModel.objects()

    #     meta = args.get('meta', {})
    #     not_null = meta.get('not_null')

    #     if not_null:
    #         qs = qs.filter(
    #             __raw__={f'json_metadata.{not_null}': {'$exists': True}}
    #         )

    #     return qs

    def resolve_market(self, info, host):
        return MarketModel.objects(host=host).first()

    def resolve_markets(self, info, args):
        qs = MarketModel.objects()
        # sort_type = args.get('sorttype', 'is1min')
        
        # qs = qs.filter(is1min = True)

        # qs = qs.filter(
        #         __raw__={f'cost': {'$exists': True}}
        #     )

        # print(qs)
        # for key in qs:
        #     pprint(getmembers(key))
        
        # # qs = qs.filter(
        # #     __raw__={f'json_metadata.{not_null}': {'$exists': True}}
        # # )
        return qs;

    # def resolve_account_authority(self, info, account):
    #     return AccountAuthorityModel.objects(account=account).first()