from django.db import models

# Create your models here.
# 1.模型类需要继承自models.Modal
# 2.系统会自动增加主键---id
class BookInfo(models.Model):
    name=models.CharField(max_length=10)


    #显示书名字
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)