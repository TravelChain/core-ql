from contextlib import suppress

from mongoengine.base.datastructures import BaseDict
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene.types.generic import GenericScalar
from common.utils import find_user, count_users
from badges.models import (
    BadgeModel, BadgeTypeModel
)
from levels.models import (    LevelModel    )

from common.utils import prepare_json
from common.types import GeometryObjectType
from common.fields import CustomMongoengineConnectionField
from pprint import pprint


class BadgeType(MongoengineObjectType):
    class Meta:
        model = BadgeTypeModel
        interfaces = (Node, )



class Badge(MongoengineObjectType):
    badges = graphene.List('badges.types.Badge', 
                             first=graphene.Int(),
                             last=graphene.Int(),
                             blockchain=graphene.String(required=True)
                             )

    badgetype = graphene.List('badges.types.BadgeType',
                             first=graphene.Int(),
                             last=graphene.Int(),

                             )

    

    def resolve_badgetype(self, info):
        qs = BadgeTypeModel.objects(ownid = self.badgetype, blockchain = self.blockchain)
        return qs;

    def resolve_badges(self, info):
        qs = BadgeModel.objects(blockchain = self.blockchain)
        #TODO find badges and construct
        return qs;
    
    class Meta:
        model = BadgeModel
        interfaces = (Node, )




    