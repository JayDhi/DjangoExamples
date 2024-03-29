# -*- coding: utf-8 -*-
""" 
@version: v1.0 
@author: andy 
@license: Apache Licence  
@contact: 93226042@qq.com 
@site:  
@software: PyCharm 
@file: myfilter.py 
@time: 2018/6/26 14:59 
"""


import django_filters
from django.db.models import Q

from .models import Article,Item

class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    文章的过滤类
    """
    author = django_filters.CharFilter(field_name='author', help_text="作者")
    status = django_filters.ChoiceFilter(field_name='status', help_text="状态")
    publish_date = django_filters.DateTimeFilter(field_name='publish_date', help_text="发布时间")
    item = django_filters.CharFilter(field_name='item', help_text="分类")
    tags = django_filters.CharFilter(field_name='tags', help_text="标签")
    # 其中method指向自己定义的过滤函数，label用于标识在测试API界面中的过滤界面字段，categorys控制查询字段
    categorys  = django_filters.NumberFilter(method='item_categorys_filter', help_text="大类")
  #  top_category = django_filters.NumberFilter(method='item_categorys_filter')

    def item_categorys_filter(self, queryset, name, value):
         return queryset.filter(item__categorys=value)


    class Meta:
        model = Article
        fields = ['author', 'status', 'publish_date', 'is_active', 'item','categorys', 'tags']