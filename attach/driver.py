33
from nova import block_device

from nova import utils as nova_utils之后
from nova.virt import block_device as driver_block_device

from nova.virt import images之后
from nova import volume
from nova.volume import encryptors

倒数第二行
from novadocker.virt.docker import utils as docker_utils



docker_volume_drivers = [
    'iscsi=novadocker.virt.docker.volume.DockerISCSIVolumeDriver',
]


        self._initiator = None
        self._fc_wwnns = None
        self._fc_wwpns = None
        self._volume_api = volume.API()
        self.volume_drivers = driver.driver_dict_from_config(
            self._get_volume_drivers(), self)
            
    def _get_volume_drivers(self):
        return docker_volume_drivers
        
    def _start_container(self, container_id, instance, network_info=None,
                         devices=None):
        binds = self._get_key_binds(container_id, instance)
        dns = self._extract_dns_entries(network_info)

        self.docker.start(container_id, binds=binds, dns=dns,
                          devices=devices)
                          

    def _get_volume_driver(self, connection_info):
        driver_type = connection_info.get('driver_volume_type')
        if driver_type not in self.volume_drivers:
            raise exception.VolumeDriverNotFound(driver_type=driver_type)
        return self.volume_drivers[driver_type]

    def _connect_volume(self, connection_info, disk_info):
        driver = self._get_volume_driver(connection_info)
        driver.connect_volume(connection_info, disk_info)

    def _disconnect_volume(self, connection_info, disk_dev):
        driver = self._get_volume_driver(connection_info)
        return driver.disconnect_volume(connection_info, disk_dev)

    def _get_volume_config(self, connection_info, disk_info):
        driver = self._get_volume_driver(connection_info)
        return driver.get_config(connection_info, disk_info)

    def _get_volume_encryptor(self, connection_info, encryption):
        encryptor = encryptors.get_volume_encryptor(connection_info,
                                                    **encryption)
        return encryptor

    def _get_guest_storage_config(self, context, block_device_info,
                                  reboot=False):
        devices = []
        block_device_mapping = driver.block_device_info_get_mapping(
            block_device_info)

        LOG.info(_LI('block_device_mapping %s'), block_device_mapping)
        for vol in block_device.get_bdms_to_connect(block_device_mapping):
            connection_info = vol['connection_info']
            vol_dev = block_device.prepend_dev(vol['mount_device'])
            info = {'dev': vol['mount_device']}
            self._connect_volume(connection_info, info)
            device_path = connection_info['data'].get('device_path')
            if device_path:
                real_path = os.path.realpath(device_path)
                devices.append(real_path + ':' + vol['mount_device'])
            bdm = objects.BlockDeviceMapping.get_by_volume_id(
                context, connection_info['data']['volume_id'])
            driver_bdm = driver_block_device.DriverVolumeBlockDevice(bdm)
            driver_bdm['connection_info'] = connection_info
            driver_bdm.save()
        return devices

    def get_volume_connector(self, instance):
        if self._initiator is None:
            self._initiator = docker_utils.get_iscsi_initiator()
            if not self._initiator:
                LOG.debug('Could not determine iscsi initiator name',
                          instance=instance)

        if self._fc_wwnns is None:
            self._fc_wwnns = docker_utils.get_fc_wwnns()
            if not self._fc_wwnns or len(self._fc_wwnns) == 0:
                LOG.debug('Could not determine fibre channel '
                          'world wide node names',
                          instance=instance)

        if self._fc_wwpns is None:
            self._fc_wwpns = docker_utils.get_fc_wwpns()
            if not self._fc_wwpns or len(self._fc_wwpns) == 0:
                LOG.debug('Could not determine fibre channel '
                          'world wide port names',
                          instance=instance)

        connector = {'ip': CONF.my_block_storage_ip,
                     'host': CONF.host}

        if self._initiator:
            connector['initiator'] = self._initiator

        if self._fc_wwnns and self._fc_wwpns:
            connector["wwnns"] = self._fc_wwnns
            connector["wwpns"] = self._fc_wwpns

        return connector
        
    def spawn
    
        devices = self._get_guest_storage_config(context, block_device_info)
        self._start_container(container_id, instance, network_info, devices)
