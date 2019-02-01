from contextlib import suppress

from mongoengine.base.datastructures import BaseDict
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene.types.generic import GenericScalar

from market.models import (
    MarketModel,
)

from common.utils import prepare_json
from common.types import GeometryObjectType


class Market(MongoengineObjectType):
    class Meta:
        model = MarketModel
        interfaces = (Node,)

    