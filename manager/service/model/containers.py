from .client import Client
from manager import models
import docker

'''
    接收containers接口的调用,实现具体功能
'''


class Containers(Client):
    def __init__(self, container_id=None, container_name=None):
        super(Containers, self).__init__()
        self.sig = container_id if container_id else container_name
        self.params = ['image', 'command', 'auto_remove', 'blkio_weight_device', 'blkio_weight',
                       'cap_add', 'cap_drop', 'cpu_count', 'cpu_percent', 'cpu_period', 'cpu_quota',
                       'cpu_shares', 'cpuset_cpus' 'cpuset_mems', 'detach', 'device_cgroup_rules',
                       'device_read_bps', 'device_read_iops', 'device_write_bps', 'device_write_iops',
                       'devices', 'dns', 'dns_opt', 'dns_search', 'domainname', 'entrypoint', 'environment',
                       'extra_hosts', 'group_add', 'healthcheck', 'hostname', 'init', 'init_path',
                       'ipc_mode', 'isolation', 'labels', 'links', 'log_config', 'mac_address',
                       'mem_limit', 'mem_swappiness', 'memswap_limit', 'mounts', 'name', 'nano_cpus',
                       'network', 'network_disabled', 'network_mode', 'oom_kill_disable', 'oom_score_adj',
                       'pid_mode', 'pids_limit', 'platform', 'ports', 'privileged', 'publish_all_ports',
                       'read_only', 'remove', 'restart_policy', 'security_opt', 'shm_size', 'stdin_open',
                       'stdout', 'stderr', 'stop_signal', 'storage_opt', 'stream', 'sysctls', 'tmpfs',
                       'tty', 'ulimits', 'user', 'userns_mode', 'volume_driver', 'volumes', 'volumes_from',
                       'working_dir', 'runtime']

    def containers_create(self):
        param = self.params
        container = self.containers.create(image=param['image'], command=param['command'])
        create_res = {
            'name': container.name,
            'id': container.id,
            'status': container.status
        }
        return create_res

    def containers_run(self, **kwargs):
        param = self.params
        k = kwargs
        container = self.containers.run(image=param['image'], command=param['command'])
        return self.containers.run()

    def del_containers(self, container_id=None, container_name=None):
        sig = container_id if container_id else container_name
        if sig:
            container = self.containers.get(sig)
            container.stop()
            container.remove()
            self.del_container_info(sig)
        return self.containers_prune()

    def del_container_info(self, container):
        will_del = models.DockerContainer.objects.filter(container)
        will_del.delete()
        return 0

    def containers_info(self):
        container_info = self.containers.list(all=True)  # 得到所有容器信息（包括为未运行的）

        res = {
            'info': container_info,
        }
        return res

    def put_containers_info(self):
        # 将容器信息存放到表中
        containers_all_info = self.containers_info()['info']
        for unit in containers_all_info:
            if models.DockerContainer.objects.filter(unit.attrs['Id']):
                continue
            res = {
                'container_id': unit.attrs['Id'],
                'container_names': unit.attrs['Names'],
                'image_name': unit.attrs['Image'],
                'image_id': unit.attrs['ImageID'],
                'command': unit.attrs['Command'],
                'container_created': unit.attrs['Created'],
                'container_ports': unit.attrs['Ports'],
                'container_labels': unit.attrs['Labels'],
                'container_state': unit.attrs['State'],
                'container_status': unit.attrs['Status'],
                'host_config': unit.attrs['HostConfig'],
                'network_settings': unit.attrs['NetworkSettings'],
            }
            models.DockerContainer.objects.create(res)
            raise 0

    def containers_prune(self):
        unused_container = self.containers.prune()
        self.del_container_info(unused_container['ID'])

    def get_container_info(self):
        info = self.containers_info()['info']
        return info

    def container_service(self, con_id=None, con_name=None, operation='status'):
        # 用于操作已经存在的容器 start stop restart 并返回执行后的状态
        params = {'operation': operation,
                  'con_id': con_id,
                  'con_name': con_name,
                  }
        if params['operation'] not in ['start', 'stop', 'restart', 'status']:
            raise 0
        sig = params['con_id'] if params['con_id'] else params['con_name']
        container = self.containers.get(sig)
        if params['operation'] == 'start':
            container.start()
        if params['operation'] == 'stop':
            container.stop()
        if params['operation'] == 'restart':
            container.restart()
        # 返回该容器处理后的状态
        return self.containers.get(sig).status

    def rename_containers(self, name=None, container_id=None, container_name=None):
        sig = container_id if container_id else container_name
        name = name
        if name:
            if sig and models.DockerContainer.objects.filter(sig):
                container = self.containers.get(sig)
                container.rename(name=name)
                # todo
                models.DockerContainer.objects.filter(sig).update()
                return 0
            return 'wrong id or name'
        return 'no name'




