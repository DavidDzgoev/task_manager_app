from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Task, User


class TaskListSerializer(serializers.ModelSerializer):
    """Task List"""

    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True, many=True)

    class Meta:
        model = Task
        fields = ("id", "owner", "name", "deadline")


class TaskDetailSerializer(serializers.ModelSerializer):
    """Specific Task"""

    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True, many=True)

    class Meta:
        model = Task
        fields = "__all__"


class TaskCreateSerializer(serializers.ModelSerializer):
    """Task Creation"""

    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, queryset=User.objects.all(), many=True)

    class Meta:
        model = Task
        fields = "__all__"


class TaskDeleteSerializer(serializers.ModelSerializer):
    """Task Creation"""

    owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, queryset=User.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ("id", "owner")


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
