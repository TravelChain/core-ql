import graphene


from levels.types import Power
from levels.models import PowerModel
from badges.models import BadgeModel
from levels.types import Level, Host
from levels.models import LevelModel, HostModel
from common.fields import CustomMongoengineConnectionField
from pprint import pprint
from inspect import getmembers


class PowerQuery(graphene.ObjectType):
    # powers = graphene.Field(Power)
    powers = CustomMongoengineConnectionField(Power, minpower = graphene.Int())

    # powers = graphene.List('levels.types.Power',
    #                          blockchain=graphene.String(required=True),
    #                          minpower=graphene.Int(),
    #                          first=graphene.Int(),
    #                          last=graphene.Int())

    badges = graphene.List('badges.types.Badge', first=graphene.Int(),
                             last=graphene.Int(),
                             host=graphene.String()
                             )

    def resolve_badges(self, info, host):
        if (host):
            qs = BadgeModel.objects(blockchain = self.blockchain, username = self.username, host = host)
        else:
            qs = BadgeModel.objects(blockchain = self.blockchain, username = self.username)
        #TODO find badges and construct
        return qs;

    
    def resolve_powers(self, info, args):

        minpower = args.get('minpower', 0)
                
        # row = {f'power': {'$gte': minpower}}
        # print(row)

        qs = PowerModel.objects(__raw__={f'power': {'$gte': minpower}})

        # qs = PowerModel.objects()
        # qs = qs.filter(
        #     __raw__={f'power': {'$gte': power}}
        # )
        return qs;



class HostQuery(graphene.ObjectType):
    hosts = CustomMongoengineConnectionField(Host)

    def resolve_hosts(self, info, args):
        qs = HostModel.objects()
        return qs;

class LevelQuery(graphene.ObjectType):
    level = graphene.Field(Level, username=graphene.String(), blockchain=graphene.String(required = True))
    levels = CustomMongoengineConnectionField(Level)

    # powers = CustomMongoengineConnectionField(Power)

    # def resolve_powers(self, info, args):
    #     qs = PowerModel.objects()
    #     return qs;
        
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

    def resolve_level(self, info, username, blockchain):
        return LevelModel.objects(username=username, blockchain = blockchain).first()

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