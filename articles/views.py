from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer, ArticleCreateSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        author = get_object_or_404(Article, author=request.author)
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save(author=request.author)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)