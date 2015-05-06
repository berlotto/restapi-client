# -*- encoding: utf-8 -*-
#
# THE RESTAPI GENERIC CLIENT CONSUMER
# Author: Sergio Berlotto <sergio.berlotto@gmail.com>
#

from distutils.core import setup

setup(
    name="restapi-client",
    description="Lib for call RestApi services",
    version="0.0.2",
    author="Sérgio Berlotto Junior",
    author_email="sergio.berlotto@gmail.com",
    url="https://github.com/berlotto/restapi-client",
    license='GPLv3',
    keywords='restapi client generic restfull',
    packages=['restapi'],
    install_requires=['requests>=2.7.0', 'ujson>=1.33'],
)
