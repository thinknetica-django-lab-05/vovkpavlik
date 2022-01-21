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

    def post(self, request):
        ad = request.data.get("ad")
        # Create an article from the above data
        serializer = AdSerializer(data=ad)
        if serializer.is_valid(raise_exception=True):
            ad_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(ad_saved.title)})
