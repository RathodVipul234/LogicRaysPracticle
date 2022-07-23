"""
    - schema file for GraphQL
"""
import graphene
from graphene_django import DjangoObjectType
from app.models import Product, Order, Brand, Category

class ProductType(DjangoObjectType):
    """
        -ProductType class
    """
    class Meta:
        """
            meta class for productType
        """
        model = Product
        fields = ["id", "name","category","brand","price","qty", "image"]


class CategoryType(DjangoObjectType):
    """
        CategoryType class
    """
    class Meta:
        """
            meta class for CategoryType
        """
        model = Category
        fields = ["id", "name"]

class BrandType(DjangoObjectType):
    """
        - BrandType class
    """
    class Meta:
        """
            - meta class for BrandType
        """
        model = Brand
        fields = ["id", "name"]


class OrderType(DjangoObjectType):
    """
        - OrderType class
    """
    class Meta:
        """
            Meta class for OrderType
        """
        model = Order
        fields = ["id","name","timestamp","placed","total_price","total_qty","products"]


class Query(graphene.ObjectType):
    """
        Graphql Query for getting list of all products and get single product by ID
    """
    all_orders = graphene.List(OrderType)
    order_by_id = graphene.Field(OrderType, id=graphene.Int())

    def resolve_all_orders(root, info):
        """
            - returning all orders
        """
        return Order.objects.all()

    def resolve_order_by_id(root, info, id):
        """
            - returning order by ID
        """
        try:
            return Order.objects.get(id=id)
        except Order.DoesNotExist:
            return None


schema = graphene.Schema(query = Query)
