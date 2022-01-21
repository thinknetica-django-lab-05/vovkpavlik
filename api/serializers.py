from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from main.models import Ad, Category, Seller


# class AdSerializer(serializers.Serializer):
#     seller = serializers.CharField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     category = serializers.CharField()
#     tags = serializers.ListField()
#     description = serializers.CharField()
#     price = serializers.IntegerField(min_value=0)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     is_archive = serializers.BooleanField()
#
    # def create(self, validated_data):
    #     return Ad.objects.create(**validated_data)
#


class AdSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model = Ad
        fields = [
            "seller", "name", "category", "tags", "description",
            "price", "created_at", "updated_at", "is_archive"
        ]

    def create(self, validated_data):
        validated_data['category'] = Category.objects.get(name="Музыка")
        return Ad.objects.create(**validated_data)
