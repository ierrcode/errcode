#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import find_packages, setup

setup(
    name='errcode',
    version="0.1.1",
    description='Error-Detecting/Correcting Codes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Zhiqing Xiao',
    author_email='xzq.xiaozhiqing@gmail.com',
    url='http://github.com/ierrcode/errcode/',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['data/*.csv']},
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
    ],
)
