from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import AdListSerializer,  CategoryListSerializer, SellerListSerializer, AdPictureSerializer
from main.models import Ad, Seller, Category, AdPicture


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerListSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


class AdPictureViewSet(viewsets.ModelViewSet):
    queryset = AdPicture.objects.all()
    serializer_class = AdPictureSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


# class SmallResultsSetPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#
#
# class AdViewSet(viewsets.ModelViewSet):
#     queryset = Ad.objects.all()
#     serializer_class = AdDetailSerializer
#     pagination_class = SmallResultsSetPagination
#     filterset_fields = ["category"]
#
    # def get_serializer_class(self):
    #     if self.action in ["list"]:
    #         return AdListSerializer
    #     return super().get_serializer_class()
#
#     def create(self, request, *args, **kwargs):
#         seller = Seller.objects.get(user=self.request.user)
#         category = Category.objects.get(name=request.data['category'])
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(seller=seller)
#         serializer.save(category=category)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def update(self, request, *args, **kwargs):
#         seller = Seller.objects.get(user=self.request.user)
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         if instance.seller == seller:
#             serializer.is_valid(raise_exception=True)
#             self.perform_update(serializer)
#             return Response(serializer.data)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
#
#     def destroy(self, request, *args, **kwargs):
#         seller = Seller.objects.get(user=self.request.user)
#         instance = self.get_object()
#         if instance.seller == seller:
#             self.perform_destroy(instance)
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
