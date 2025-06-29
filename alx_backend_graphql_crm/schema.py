from crm.schema import Query as CrmQuery
import graphene

class Query(CrmQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
