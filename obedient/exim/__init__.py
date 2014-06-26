from dominator.entities import *


def create(ships, port=25, repository='yandex/exim'):
    db_volume = DataVolume(name='db', dest='/var/spool/exim4/db')
    image = Image(repository)
    return [Container(
        name='exim',
        ship=ship,
        image=image,
        memory=200*1024*1024,
        ports={'smtp': 25},
        extports={'smtp': port},
        volumes=[db_volume],
    ) for ship in ships]
