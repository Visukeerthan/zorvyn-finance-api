from rest_framework import serializers
from .models import FinancialEntry, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class FinancialEntrySerializer(serializers.ModelSerializer):
    # We make 'user' read_only so the API user can't "fake" the owner
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FinancialEntry
        fields = '__all__'