from django.shortcuts import render
from .models import News,NewsCategory
from django.conf import settings
from utils import restful
from .serializers import NewsSerializer
from django.http import Http404

def index(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.order_by('-pub_time')[0:count]
    categories = NewsCategory.objects.all()
    context = {
        'newses': newses,
        'categories': categories,
    }
    return render(request,'news/index.html',context=context)

def news_list(request):
    # 通过p参数，来指定要获取第几页的数据
    # 并且这个p参数，是通过查询字符串的方式传过来的/news/list/?p=2
    page = int(request.GET.get('p',1))
    category_id = int(request.GET.get('category_id',0))
    # 分类为0：代表不进行任何分类，直接按照时间倒序排序
    #category_id = int(request.GET.get('category_id',0))
    # 0,1
    # 2,3
    # 4,5
    start = (page-1)*settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT

    if category_id == 0:
         newses = News.objects.all()[start:end]
    else:
        newses = News.objects.filter(category_id=category_id)[start:end]
    serializer = NewsSerializer(newses,many=True)
    data = serializer.data
    return restful.result(data=data)


def news_detail(request,news_id):
    try:
        news = News.objects.get(pk=news_id)
        context = {
            'news': news
        }
        return render(request,'news/news-detail.html',context=context)
    except:
        raise Http404
