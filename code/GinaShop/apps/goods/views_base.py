# -*- coding: utf-8 -*-
# @Time    : 2018/1/24
# @Author  : whoiszxl
# @Site    : 
# @File    : views_base.py
# @Software: PyCharm

from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django view获取商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        import json
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        return JsonResponse(json_data, safe=False)
