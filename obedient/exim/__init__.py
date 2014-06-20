from dominator import *

@aslist
def make_containers(ships, port=25, repository='yandex/exim'):
    db_volume = DataVolume(name='db', dest='/var/spool/exim4/db')
    for ship in ships:
        yield Container(
            name='exim',
            ship=ship,
            image=Image(repository),
            memory=200*1024*1024,
            ports={'smtp': 25},
            extports={'smtp': port},
            volumes=[db_volume],
        )
