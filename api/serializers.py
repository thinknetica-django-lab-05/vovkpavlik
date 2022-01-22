from rest_framework import serializers

from main.models import Ad


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
        return Ad.objects.create(**validated_data)



