from rest_framework import serializers

from main.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    """
        Сериализитор для списка объявлений
        с частичной информацией.
    """
    category = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model = Ad
        fields = ["id", "seller", "name", "category", "price", "is_archive"]


class AdDetailSerializer(serializers.ModelSerializer):
    """
        Сериализитор для конкретного объявления
        с полной информацией.
    """
    category = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model = Ad
        fields = [
            "seller", "name", "category", "tags", "description",
            "price", "created_at", "updated_at", "is_archive"
        ]
