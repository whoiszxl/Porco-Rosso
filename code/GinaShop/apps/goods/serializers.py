# -*- coding: utf-8 -*-
# @Time    : 2018/1/24
# @Author  : whoiszxl
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
