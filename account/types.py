from contextlib import suppress

from mongoengine.base.datastructures import BaseDict
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene.types.generic import GenericScalar

from account.models import (
    AccountModel,
)
from levels.models import (
    PowerModel, LevelModel
)

from badges.models import (
    BadgeModel
)

from common.utils import prepare_json
from common.types import GeometryObjectType


class AccountLocation(graphene.ObjectType):
    properties = GenericScalar()
    geometry = graphene.Field(GeometryObjectType)

    def resolve_properties(self, info):
        return self.get('properties', {})

    def resolve_geometry(self, info):
        return self.get('geometry', {})


class MapalaProfile(graphene.ObjectType):
    avatar = graphene.String()
    location = graphene.Field(AccountLocation)

    def resolve_avatar(self, info):
        return self.get('avatar')

    def resolve_location(self, info):
        return self.get('location', {})


class AccountProfile(graphene.ObjectType):
    profile_image = graphene.String()
    website = graphene.String()
    cover_image = graphene.String()
    
    def resolve_meta(self, info):
        return prepare_json(self.meta)

    def resolve_cover_image(self, info):
        with suppress(KeyError):
            return self['cover_image']

    def resolve_website(self, info):
        with suppress(KeyError):
            return self['website']

    def resolve_profile_image(self, info):
        with suppress(KeyError):
            return self['profile_image']


class AccountMeta(graphene.ObjectType):
    profile = graphene.Field(AccountProfile)
    
    def resolve_profile(self, info):
        return self.get('profile', {})


class Account(MongoengineObjectType):
    meta = graphene.Field(AccountMeta)
    json_metadata = GenericScalar()

    powers = graphene.List('levels.types.Power',
                             first=graphene.Int(),
                             last=graphene.Int(),
                             host=graphene.String(),
                             minpower = graphene.Int()
                             )

    badges = graphene.List('badges.types.Badge', first=graphene.Int(),
                             last=graphene.Int(),
                             host=graphene.String()
                             )

    avatar = graphene.String()

    nickname = graphene.String()


    def resolve_nickname(self, info):
        user = LevelModel.objects(username=self.username, blockchain = self.blockchain).first()
        meta = prepare_json(user.meta)
        
        if 'nickname' in meta:
            return meta['nickname']
        else:
            return ""   

    def resolve_avatar(self, info):
        user = LevelModel.objects(username=self.username, blockchain = self.blockchain).first()
        meta = prepare_json(user.meta)
        
        if 'img' in meta:
            return meta['img']
        else:
            return "/ava.png"    


    def resolve_badges(self, info, host):
        if (host):
            qs = BadgeModel.objects(blockchain = self.blockchain, username = self.username, host = host)
        else:
            qs = BadgeModel.objects(blockchain = self.blockchain, username = self.username)
        #TODO find badges and construct
        return qs;

    
    def resolve_powers(self, info, host):
        
        if (host):
            qs = PowerModel.objects(blockchain=self.blockchain, username = self.username, host=host)
        else:
            qs = PowerModel.objects(blockchain=self.blockchain, username = self.username)
            
        return qs;


    def resolve_json_metadata(self, info):
        User  = LevelModel.objects(username = self.username, blockchain = self.blockchain)
        return prepare_json(self.meta)

    class Meta:
        model = AccountModel
        interfaces = (Node,)

    def resolve_meta(self, info):
        if isinstance(self.meta, BaseDict):
            return self.meta
        else:
            return {}
