from django.shortcuts import render

# Create your views here.
#定义视图函数
# 视图函数的第一个参数:
# 1.接收请求
# 2.返回一个响应

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
#模拟数据查询
    context={
        'name':'双十一到了,点击此处有惊喜'
    }
    return render(request,'book/index.html',context)



    # return HttpResponse('ok')