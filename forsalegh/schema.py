import graphene

import classifieds.schema 

class Query(classifieds.schema.Query, graphene.ObjectType):
    #This class inherits from multiple queries
    pass

schema = graphene.Schema(query=Query)