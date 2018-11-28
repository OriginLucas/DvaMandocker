from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_http_methods
# Create your views here.
from monitor.service.api import a


@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, "index.html")


# 给agent提供监控项列表
@require_http_methods(["GET"])
def active_items(request):
    return HttpResponse(0)


# 获取监控信息
@require_http_methods(["POST"])
def recv_msg(request):
    res = request.POST()
    return HttpResponse(0)


# 获取缓存文件
@require_http_methods(["POST"])
def recv_file(request):
    res = request.POST()
    return HttpResponse(0)
