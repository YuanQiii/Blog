from rest_framework import serializers

from app01.models import SayName, Article, Comment, Archives, ArticleContent, Opinion


class SayNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SayName
        fields = ['firstName', 'lastName']


class ArticleSerializer(serializers.ModelSerializer):
    # article_comment = serializers.IntegerField(source=Comment.pk)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleContent
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # article_comments = serializers.IntegerField(source=Article.pk)

    class Meta:
        model = Comment
        fields = '__all__'


class ArchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archives
        fields = '__all__'


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'
