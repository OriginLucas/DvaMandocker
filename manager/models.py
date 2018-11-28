from django.db import models

# Create your models here.


class DockerImages(models.Model):
    id = models.AutoField(primary_key=True)
    containers = models.CharField(max_length=128)
    image_created = models.IntegerField()  # 记录为时间戳
    image_id = models.CharField(max_length=128)
    image_lab = models.CharField(max_length=128)
    parent_id = models.CharField(max_length=128)
    repo_digests = models.CharField(max_length=128)
    repo_tags = models.CharField(max_length=128)
    shared_size = models.CharField(max_length=128)  # 处理
    size = models.CharField(max_length=128)  # 处理
    virtual_size = models.CharField(max_length=128)  # 处理


class DockerContainer(models.Model):

#     id = models.AutoField(primary_key=True)
#     container_id = models.CharField(max_length=128)
#     container_names = models.CharField(max_length=128)
#     image_name = models.CharField(max_length=128)
#     image_id = models.ForeignKey('DockerImages', on_delete=models.SET_NULL)
#     command = models.CharField(max_length=128)
#     container_created = models.IntegerField()
#     container_ports = models.CharField(max_length=128)
#     container_labels = models.CharField(max_length=128)
#     container_state = models.CharField(max_length=128)
#     container_status = models.CharField(max_length=128)
#     host_config = models.CharField(max_length=128)
#     network_settings = models.CharField(max_length=1024)
    pass


class DockerNetworks(models.Model):
    id = models.AutoField(primary_key=True)
    network_id = models.CharField(max_length=128)
    network_name = models.CharField(max_length=128)
    network_created = models.CharField(max_length=128)
    network_scop = models.CharField(max_length=128)
    network_driver = models.CharField(max_length=128)
    network_enableIPv6 = models.BinaryField()
    network_config = models.CharField(max_length=1024)
    # todo
