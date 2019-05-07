import graphene


from badges.types import Badge
from badges.models import BadgeModel
from common.fields import CustomMongoengineConnectionField
from pprint import pprint
from inspect import getmembers

class BadgesQuery(graphene.ObjectType):
    badges = CustomMongoengineConnectionField(Badge)

    def resolve_badges(self, info, args):
        qs = BadgeModel.objects()
        return qs;