import json
import time

from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from app01 import serializers, models
from app01.models import SayName, Article, Comment, Archives, ArticleContent, Opinion
from app01.serializers import SayNameSerializer, ArticleSerializer, CommentSerializer, ArchivesSerializer, \
    ArticleContentSerializer, OpinionSerializer


# class MyEncoder(json.JSONEncoder):
#
#     def default(self, obj):
#         """
#         只要检查到了是bytes类型的数据就把它转为str类型
#         :param obj:
#         :return:
#         """
#         if isinstance(obj, bytes):
#             return str(obj, encoding='utf-8')

# class VisitCountMidlleware(View):
#     def get(self, request):
#         stats = cache.get('stats')
#         if stats:
#             current_time = time.time()
#             curr_ips = [k for k, v in stats.items() if int(v[0]) - current_time < 60]
#             count = []
#             for ip in curr_ips:
#                 count.append(stats[ip][1])
#         else:
#             curr_ips = []
#             count = []
#         return render(request, "stats_flow.html", locals())


def hello(request):
    if request.method == 'GET':
        sayname = SayName.objects.all()
        serializer = SayNameSerializer(sayname, many=True)
        return JsonResponse(serializer.data, safe=False)


def article(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class CommentView(APIView):
    def post(self, request, *args, **kwargs):
        ser = CommentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
        else:
            return JsonResponse(ser.errors)


def getcomments(request):
    if request.method == 'GET':
        commnets = Comment.objects.all()
        commnets_ser = CommentSerializer(commnets, many=True)
        return JsonResponse(commnets_ser.data, safe=False)


def articleinfo(request, pk):
    if request.method == 'GET':
        info = Article.objects.filter(id=pk)
        info_ser = ArticleSerializer(info, many=True)
        return JsonResponse(info_ser.data, safe=False)


def getarchives(request):
    if request.method == 'GET':
        content = Archives.objects.all()
        content_ser = ArchivesSerializer(content, many=True)
        return JsonResponse(content_ser.data, safe=False)


def archives(request, pk):
    if request.method == 'GET':
        content = Archives.objects.filter(id=pk)
        content_ser = ArchivesSerializer(content, many=True)
        return JsonResponse(content_ser.data, safe=False)


def content(request, pk):
    if request.method == 'GET':
        contents = ArticleContent.objects.filter(article_id=pk)
        contents_ser = ArticleContentSerializer(contents, many=True)
        return JsonResponse(contents_ser.data, safe=False)


class CountView(APIView):
    def put(self, request, pk):
        instance = Article.objects.get(id=pk)
        ser = ArticleSerializer(instance, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            print(ser)
            return JsonResponse(ser.data)
        else:
            return JsonResponse(ser.errors)


class OpinionView(APIView):
    def get(self, request, pk):
        opinion = Opinion.objects.filter(article_id=pk)
        opinion_ser = OpinionSerializer(opinion, many=True)
        return JsonResponse(opinion_ser.data, safe=False)


class PostOpinion(APIView):
    def post(self, request):
        print(request.data)
        ser = OpinionSerializer(data=request.data, many=False)
        print(ser)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
        else:
            return JsonResponse(ser.errors)


def getopinion(request):
    if request.method == 'GET':
        opinion = Opinion.objects.all()
        opinion_ser = OpinionSerializer(opinion, many=True)
        return JsonResponse(opinion_ser.data, safe=False)
