from dominator.entities import *


def create(ships, port=25):
    db_volume = DataVolume('/var/spool/exim4/db')
    image = SourceImage(
        name='exim',
        parent=Image('yandex/trusty'),
        scripts=[
            'echo -e "exim4-config\texim4/dc_local_interfaces\tstring\t0.0.0.0\\n\
exim4-config\texim4/dc_eximconfig_configtype\tstring\tinternet site; mail is sent and received directly using SMTP\\n\
exim4-config\texim4/dc_relay_domains\tstring\t*" | debconf-set-selections',
            'apt-get install -y exim4',
        ],
        ports={'smtp': 25},
        command='/usr/sbin/exim4 -bdf -v -q30m',
    )
    return [Container(
        name='exim',
        ship=ship,
        image=image,
        memory=200*1024*1024,
        ports=image.ports,
        extports={'smtp': port},
        volumes={'data': db_volume},
    ) for ship in ships]
