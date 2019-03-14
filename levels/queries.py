import graphene

from levels.types import Level, Host
from levels.models import LevelModel, HostModel
from common.fields import CustomMongoengineConnectionField
from pprint import pprint
from inspect import getmembers

class HostQuery(graphene.ObjectType):
    hosts = CustomMongoengineConnectionField(Host)

    def resolve_hosts(self, info, args):
        qs = HostModel.objects()
        return qs;

class LevelQuery(graphene.ObjectType):
    level = graphene.Field(Level, username=graphene.String())
    levels = CustomMongoengineConnectionField(Level)

    # lev = graphene.Int(0)
    
    # def resolve_accounts(self, info, args):
    #     qs = AccountModel.objects()

    #     meta = args.get('meta', {})
    #     not_null = meta.get('not_null')

    #     if not_null:
    #         qs = qs.filter(
    #             __raw__={f'json_metadata.{not_null}': {'$exists': True}}
    #         )

    #     return qs
    # def resolve_lev(self, info, args):

    #     if self.lev:
    #         return self.lev + 1
    #     else:
    #         return 1

    def resolve_level(self, info, username):
        return LevelModel.objects(username=username).first()

    def resolve_levels(self, info, args):
        qs = LevelModel.objects()
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