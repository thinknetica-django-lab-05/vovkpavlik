from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdSerializer
from main.models import Ad, Seller, Category


class AdListView(APIView):
    queryset = Ad.objects.all()

    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response({"ads": serializer.data})

    def post(self, request):
        ad = request.data.get("ad")
        serializer = AdSerializer(data=ad)
        seller = Seller.objects.get(user=self.request.user)
        category = Category.objects.get(name=ad['category'])
        if serializer.is_valid():
            serializer.save(seller=seller)
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
