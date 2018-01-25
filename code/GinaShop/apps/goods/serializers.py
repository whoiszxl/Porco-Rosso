# -*- coding: utf-8 -*-
# @Time    : 2018/1/24
# @Author  : whoiszxl
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from goods.models import Goods, GoodsCategory, HotSearchWords


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"

    sub_cat = CategorySerializer3(many=True)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"

    sub_cat = CategorySerializer2(many=True)


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = "__all__"

    category = CategorySerializer()


class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"
