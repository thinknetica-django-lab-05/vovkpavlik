from rest_framework import serializers

from main.models import Ad, Category, Seller, AdPicture


class SellerListSerializer(serializers.ModelSerializer):
    """
        Сериализитор для списка продавцов
    """

    class Meta:
        model = Seller
        fields = ["id", "user", "phone"]


class AdPictureSerializer(serializers.ModelSerializer):
    """
        Сериализитор для картинок объявлений
    """

    class Meta:
        model = AdPicture
        fields = ["id", "image"]


class AdListSerializer(serializers.ModelSerializer):
    """
        Сериализитор для списка объявлений
    """

    ad_picture = AdPictureSerializer(many=True)

    class Meta:
        model = Ad
        fields = [
            "id", "seller", "name", "category", "tags", "description",
            "price", "created_at", "updated_at", "is_archive",
            "ad_picture"
        ]

    def create(self, validated_data):
        ad_pictures_data = validated_data.pop("ad_picture")
        ad = Ad.objects.create(**validated_data)
        for ad_picture_data in ad_pictures_data:
            AdPicture.objects.create(ad=ad, **ad_picture_data)
        return ad


class CategoryListSerializer(serializers.ModelSerializer):
    """
        Сериализитор для списка категорий
    """
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
