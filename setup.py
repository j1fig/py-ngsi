from setuptools import setup
from setuptools import find_packages

import time
_version = '0.1.0.%s' % int(time.time())

_packages = find_packages(where='.')

install_requires = [
    'requests',
    'nose',
]

setup(
    name='py-ngsi',
    version=_version,
    description='NGSI 9/10 Python client',
    author='Joao Figueiredo',
    author_email='joaonvfigueiredo@gmail.com',
    url='http://brain-e.pt',
    install_requires=install_requires,
    packages=_packages,
    include_package_data=True,
)
