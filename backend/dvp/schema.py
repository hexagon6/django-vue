import graphene

import tasks.schema

class Query(tasks.schema.Query, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query)