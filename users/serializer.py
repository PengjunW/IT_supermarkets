from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    account_balance = serializers.FloatField(read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'account_balance']


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=Users.objects.all(), message='exists!')])
    password = serializers.CharField(min_length=6, max_length=12, write_only=True,
                                     error_messages={
                                         'max_length': 'too long',
                                         'min_length': 'too short',
                                     })
    confirm = serializers.CharField(min_length=6, max_length=12, write_only=True,
                                    error_messages={
                                        'max_length': 'too long',
                                        'min_length': 'too short',
                                    })
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('no equal!')
        del attrs['confirm']
        return attrs

    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'confirm', 'email']

    def create(self, validated_data):
        passwd = validated_data.pop('password')
        user = Users(**validated_data)
        user.set_password(passwd)
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']

        try:
            user = Users.objects.get(username=username)
        except:
            raise serializers.ValidationError('no user')
        else:
            if user.check_password(password):
                return attrs
            else:
                raise serializers.ValidationError('password is wrong!')

    class Meta:
        model = Users
        fields = ['username', 'password']


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=12, write_only=True,
                                     error_messages={
                                         'max_length': 'too long',
                                         'min_length': 'too short',
                                     })
    confirm = serializers.CharField(min_length=6, max_length=12, write_only=True,
                                    error_messages={
                                        'max_length': 'too long',
                                        'min_length': 'too short',
                                    })

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('no equal!')
        del attrs['confirm']
        return attrs

    class Meta:
        model = Users
        fields = ['password', 'confirm']

    def update(self, instance, validated_data):
        passwd = validated_data.pop('password')
        instance.set_password(passwd)
        instance.save()
        return instance
