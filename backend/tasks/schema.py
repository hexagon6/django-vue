import graphene
from graphene_django import DjangoObjectType

from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()