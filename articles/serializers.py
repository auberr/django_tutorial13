from rest_framework import serializers
from articles.models import Article

# 방법 1로 할경우에 author를 띄우는 방법?

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.email
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.email
    
    class Meta:
        model = Article
        fields = ("title", "content", "id", "author", "category")
    

# 방법2 
# class ArticleCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'

#         extra_kwargs={
#             'author': {'read_only':True}
#         }


# 방법 3
# class ArticleSerializer(serializers.ModelSerializer):
#     author = serializers.SerializerMethodField()

#     def get_author(self, obj):
#         return obj.author.username
    
#     class Meta:
#         model = Article
#         fields = '__all__'
    
#         extra_kwargs={
#             'author': {'read_only':True}
#         }
    # def create(self, validated_data):
    #     author = self.context["request"].user