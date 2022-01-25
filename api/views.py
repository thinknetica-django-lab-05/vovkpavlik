from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdSerializer
from main.models import Ad


class AdListView(APIView):
    queryset = Ad.objects.all()

    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response({"ads": serializer.data})
