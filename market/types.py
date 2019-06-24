from contextlib import suppress

from mongoengine.base.datastructures import BaseDict
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene.types.generic import GenericScalar

from market.models import (
    MarketModel, CoreMarketModel, RatesModel, SpiralModel
)

from common.utils import prepare_json
from common.types import GeometryObjectType

class Spiral(MongoengineObjectType):
	class Meta:
		model = SpiralModel
		interfaces = (Node, )

class Rates(MongoengineObjectType):
	class Meta:
		model = RatesModel
		interfaces = (Node, )

class CoreMarket(MongoengineObjectType):

    def resolve_open(self, info):
        return self.open / 10000

    def resolve_close(self, info):
        return self.close / 10000

    def resolve_high(self, info):
        return self.high / 10000

    def resolve_low(self, info):
        return self.low / 10000
        

        # if isinstance(self.meta, BaseDict):
        #     return prepare_json(self.meta)
        # else: 
        #     return {}
    


    class Meta:
        model = CoreMarketModel
        interfaces = (Node,)

    

class Market(MongoengineObjectType):
    class Meta:
        model = MarketModel
        interfaces = (Node,)

    