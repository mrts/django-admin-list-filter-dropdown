# encoding: utf-8

import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-list-filter-dropdown',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Use dropdowns in Django admin list filter',
    url='https://github.com/mrts/django-admin-list-filter-dropdown',
    author='Mart Sõmermaa',
    author_email="mrts.pydev at gmail dot com",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
