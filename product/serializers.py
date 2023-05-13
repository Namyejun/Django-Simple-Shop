from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Product

        fields = "__all__"  # 모든 필드를 직렬화
        # pk, 상품명, 가격만 직렬화 하고싶다면
        # field = ["pk", "product_name", "product_price"]
