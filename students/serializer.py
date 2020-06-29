from rest_framework import serializers

from students.models import Students


class StuSerializer(serializers.Serializer):
    name=serializers.CharField(min_length=2,max_length=6)
    age=serializers.IntegerField()
    sex=serializers.IntegerField()
    phone=serializers.IntegerField()

    sex=serializers.SerializerMethodField()
    def get_sex(self,obj):
        return obj.get_sex_display()

    def create(self, validated_data):
        return Students.objects.create(**validated_data)