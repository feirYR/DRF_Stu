from django.urls import path
from students import views
urlpatterns=[
    path('stu_view/',views.StuAPIView.as_view()),
    path('stu_view/<str:id>/',views.StuAPIView.as_view())
]