import graphene

from market.types import Market
from market.models import MarketModel
from common.fields import CustomMongoengineConnectionField
from pprint import pprint
from inspect import getmembers

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