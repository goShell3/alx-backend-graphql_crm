# from crm.schema import Query as CrmQuery
# import graphene

# class Query(CrmQuery, graphene.ObjectType):
#     pass

# schema = graphene.Schema(query=Query)
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)
