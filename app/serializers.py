from rest_framework import serializers

from app.models import Region, Shop, District, Saved


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = "__all__"

    def validate(self, attrs):
        phone = attrs.get("phone")
        if len(phone) != 10:
            raise serializers.ValidationError("Неверный номер!")

        phone_codes = {312, 555, 557, 705, 707, 777}

        if int(phone[0]) != 0:
            raise serializers.ValidationError("Номер телефона должен начинаться с 0!")

        if int(phone[1: 4]) not in phone_codes:
            raise serializers.ValidationError("Неверный формат номера!")

        return attrs


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = "__all__"


class SavedSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(read_only=True)

    class Meta:
        model = Saved
        fields = "__all__"








