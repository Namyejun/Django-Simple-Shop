from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# 상품 목록 API
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all() # 쿼리 셋에는 시리얼라이즈 할 데이터
    serializer_class = ProductSerializer

# 상품 상세 API
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateAPIView : C 빼고 RUD 담당
    # CreateAPIView : C 담당
    # C(POST) - Create
    # R(READ) - Retrieve
    # U(PUT) - Update
    # D(DELETE) - Destroy
    queryset = Product.objects.all()
    serializer_class = ProductSerializer