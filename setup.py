import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='obedient.exim',
        version='1.1',
        url='https://github.com/yandex-sysmon/obedient-exim',
        license='GPLv3',
        author='Nikolay Bryskin',
        author_email='devel.niks@gmail.com',
        description='Exim4 obedient for Dominator',
        platforms='linux',
        packages=['obedient.exim'],
        namespace_packages=['obedient'],
        install_requires=['dominator >=4'],
    )
