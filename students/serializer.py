from rest_framework import serializers,exceptions

from students.models import Students


class StuSerializer(serializers.Serializer):
    name=serializers.CharField(min_length=2,max_length=6)
    age=serializers.IntegerField()
    # sex=serializers.IntegerField()
    phone=serializers.CharField()
    # phone=serializers.SerializerMethodField()
    sex=serializers.SerializerMethodField()
    def get_sex(self,obj):
        print(14,obj.get_sex_display())
        return obj.get_sex_display()

    def create(self, validated_data):
        sex=validated_data.get('sex')
        print(validated_data)
        print('create',sex)
        return Students.objects.create(**validated_data)

    def validate_name(self,value):
        if '1' in value:
            raise exceptions.ValidationError('用户名有误')
        return value

    def validate(self, attrs):
        age=attrs.get('age')
        if age>100:
            raise exceptions.ValidationError('年龄过大')
        return attrs
