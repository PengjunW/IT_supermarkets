from rest_framework import serializers
from users.models import Users
from .models import UserAddress


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['account_balance']

    def update(self, instance, validated_data):
        balance = validated_data.pop('account_balance')
        instance.account_balance += balance
        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")
