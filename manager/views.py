from manager.service.api.IImageService import ApiImages
from manager.service.api.IContainerService import ApiContainers
from manager.service.api.INetworkService import ApiNetworks
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_http_methods
from mako.template import Template

# Create your views here.


@require_http_methods(["GET", "POST"])
def image_order(request):
    image_info = ApiImages().get_image_info()
    return render(request, 'docker.html', {"images": image_info['info']})


@require_http_methods(["GET", "POST"])
def container_order(request):
    container_info = ApiContainers().get_container_info()
    print(container_info)
    return render(request, 'containers_view.html', {"containers": container_info})


@require_http_methods(["GET", "POST"])
def container_add(request):
    return render(request, 'containers_add.html')


def network_order(request):
    network_info = ApiNetworks().get_networks_info()
    print(network_info)
    return render(request, 'networks_view.html', {"networks": network_info})


@require_http_methods(["GET", "POST"])
def index(request):

    return render(request, 'index.html')


@require_http_methods(["GET", "POST"])
def login(request):

    return render(request, 'login.html')


def put(request):
    a = ApiImages().put_image_info()
    print(a)
    return HttpResponse('ok')
