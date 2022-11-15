from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer, ArticleCreateSerializer
from django_advance.permissions import RegisteredMoreThanThreeMinutesUser

# Create your views here.
class ArticleView(APIView):
    # permission_classes = [RegisteredMoreThanThreeMinutesUser]    

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        # print(request.username)
        # print(request.id)
        if not request.user.is_authenticated:
            return Response({"message":"로그인해주세요"}, 401)


        title = request.data.get("title", "")
        print(title)
        content = request.data.get("content", "")
        category = request.data.get("category", "")
        data = {"title":title, "content":content, "category":category}
        print(data)
        serializer = ArticleCreateSerializer(data=request.data)
        print(request.data)
        print(serializer)
        if serializer.is_valid(): 
            serializer.save(author=request.user)
            return Response({"message":"글 작성 완료!!"})
            # return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)