from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'

    def validate(self, data):
        name = data.get('name')

        if name and name.isdigit():
            raise serializers.ValidationError(
                {'error': 'name son bolmasligi kerak'}
            )

        return data

    def validate_income(self, value):
        if value < 0:
            raise serializers.ValidationError(
                {'error': 'income manfiy bolmasligi kerak'}
            )

        return value