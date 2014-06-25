from datetime import datetime
from dominator import *

@aslist
def create(ships, port=25, repository='yandex/exim', tag='{:d%Y%m%d}'.format(datetime.utcnow())):
    db_volume = DataVolume(name='db', dest='/var/spool/exim4/db')
    image = Image(repository, tag=tag)
    for ship in ships:
        yield Container(
            name='exim',
            ship=ship,
            image=image,
            memory=200*1024*1024,
            ports={'smtp': 25},
            extports={'smtp': port},
            volumes=[db_volume],
        )
