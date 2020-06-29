import traceback

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from students.models import Students
from students.serializer import StuSerializer


class StuAPIView(APIView):
    def get(self,request,*args,**kwargs):
        # id = kwargs.get('id')
        re=request.GET
        if re:
            id=re['id']
            print('单查', id)
            stu=Students.objects.filter(id=id)[0]
            if stu:
                stu_ser=StuSerializer(stu).data
                return Response({'status':200,'message':'查询单个学生成功','students':stu_ser})
            # return Response({'status': 500, 'message': '查询单个学生失败'})

        else:
            stu=Students.objects.all()
            stu_ser=StuSerializer(stu,many=True).data
            return Response({'status': 200, 'message': '查询所有学生成功', 'students': stu_ser})
        return Response({'status': 500, 'message': '查询失败'})

    def post(self,request,*args,**kwargs):
        try:
            stu_data=request.data
            ser=StuSerializer(data=stu_data)
            # print(32,ser)
            if ser.is_valid():
                stu=ser.save()
                return Response({'status':200,'message':'创建学生成功','student':StuSerializer(stu).data})
            return Response({'status': 500, 'message': '创建失败', 'error':ser.errors})
        except:
            traceback.print_exc()