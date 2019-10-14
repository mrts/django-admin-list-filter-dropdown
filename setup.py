# encoding: utf-8

import os
from setuptools import find_packages, setup

VERSION = '1.0.3'

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

description = 'Use dropdowns in Django admin list filter'
long_description = description
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name='django-admin-list-filter-dropdown',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description=description,
    long_description=long_description,
    url='https://github.com/mrts/django-admin-list-filter-dropdown',
    download_url='https://github.com/mrts/django-admin-list-filter-dropdown/archive/%s.zip' % VERSION,
    author='Mart Sõmermaa',
    author_email="mrts.pydev@gmail.com",
    keywords=['django', 'admin', 'filter', 'dropdown'],
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
