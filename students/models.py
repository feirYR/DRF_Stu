from django.db import models

# Create your models here.
class Students(models.Model):
    sex_choices=[
        (0,'男'),
        (1,'女')
    ]
    name=models.CharField(max_length=10)
    age=models.SmallIntegerField()
    sex=models.SmallIntegerField(choices=sex_choices,default=0)
    # sex=models.CharField(choices=sex_choices,default=0)
    phone=models.CharField(max_length=11)

    class Meta:
        db_table='stu_system'
        verbose_name='学生'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name