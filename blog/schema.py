# blog/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from .models import Post, Comment
from datetime import datetime


class PostType(DjangoObjectType):
    class Meta:
        model = Post

    def resolve_publish_date(self, info):
        return self.publish_date.strftime("%Y-%m-%d")


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        # publish_date = graphene.Date()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, title, description, author):
        post = Post(
            title=title,
            description=description,
            publish_date=datetime.now().date(),
            author=author,
        )
        post.save()
        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        description = graphene.String()
        # publish_date = datetime.now().date()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, title, description, author):
        post = Post.objects.get(pk=id)
        post.title = title
        post.description = description
        post.publish_date = datetime.now().date()
        post.author = author
        post.save()
        return UpdatePost(post=post)


class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID()
        text = graphene.String()
        author = graphene.String()

    comment = graphene.Field(CommentType)

    def mutate(self, info, post_id, text, author):
        post = Post.objects.get(pk=post_id)
        comment = Comment(post=post, text=text, author=author)
        comment.save()
        return CreateComment(comment=comment)


class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            comment = Comment.objects.get(pk=id)
            comment.delete()
            return DeleteComment(success=True)
        except Comment.DoesNotExist:
            return DeleteComment(success=False)


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.ID())
    comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, id=graphene.ID())

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_post(self, info, id):
        return Post.objects.get(pk=id)

    def resolve_comments(self, info):
        return Comment.objects.all()

    def resolve_comment(self, info, id):
        return Comment.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()


Schema = graphene.Schema(query=Query, mutation=Mutation)
