from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import generics

from .models import Goods


# Create your views here.

class GoodsListView(generics.ListAPIView):
    """
    List all Goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

