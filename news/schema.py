import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Article, Reporter


# Create a GraphQL type for the reporter model
class ReporterType(DjangoObjectType):
    class Meta:
        model = Reporter


# Create a GraphQL type for article model
class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


# Create a Query type
class Query(ObjectType):
    reporter = graphene.Field(ReporterType, id=graphene.Int())
    article = graphene.Field(ArticleType, id=graphene.Int())
    reporters = graphene.List(ReporterType)
    articles= graphene.List(ArticleType)

    def resolve_reporter(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Reporter.objects.get(pk=id)

        return None

    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Article.objects.get(pk=id)

        return None

    def resolve_reporters(self, info, **kwargs):
        return Reporter.objects.all()

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()


# Mutations - Input object types
class ReporterInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    

class ArticleInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    reporter = graphene.Field(ReporterInput)


class CreateReporter(graphene.Mutation):
    class Arguments:
        input = ReporterInput(required=True)

    ok = graphene.Boolean()
    reporter = graphene.Field(ReporterType)
    
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        reporter_instance = Reporter(name=input.name)
        reporter_instance.save()
        return CreateReporter(ok=ok, reporter=reporter_instance)

class UpdateReporter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ReporterInput(required=True)
        
    ok = graphene.Boolean()
    reporter = graphene.Field(ReporterType)
    
    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        reporter_instance = Reporter.objects.get(pk=id)
        if reporter_instance:
            ok = True
            reporter_instance.name = input.name
            reporter_instance.save()
            return UpdateReporter(ok=ok, reporter=reporter_instance)
        return UpdateReporter(ok=ok, reporter=None)


class CreateArticle(graphene.Mutation):
    class Arguments:
        input = ArticleInput(required=True)
        
    ok = graphene.Boolean()
    article = graphene.Field(ArticleType)
    
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        reporter_input = input.reporter
        reporter = Reporter.objects.get(pk=reporter_input.id)
        if reporter is None:
            return CreateArticle(ok=False, article=None)
        article_instance = Article(
            title=input.title, 
            reporter=reporter
        )
        article_instance.save()
        return CreateArticle(
            ok=ok,
            article=article_instance
        )


class UpdateArticle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ArticleInput(required=True)
        
    ok = graphene.Boolean()
    article = graphene.Field(ArticleType)
    
    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        article_instance = Article.objects.get(pk=id)
        if article_instance:
            ok = True
            reporter_input = input.reporter
            article_instance.title = input.title
            if reporter_input is not None:
                reporter = Reporter.objects.get(pk=reporter_input.id)
                article_instance.reporter = reporter
            article_instance.save()
            return UpdateArticle(
                ok=ok,
                article=article_instance
            )
        return UpdateArticle(ok=ok, article=None)
    

class Mutation(graphene.ObjectType):
    create_reporter = CreateReporter.Field()
    update_reporter = UpdateReporter.Field()
    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()
    

schema = graphene.Schema(query=Query, mutation=Mutation)
