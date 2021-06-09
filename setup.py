
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='amortization',
    version='1.0.4',
    description='Python library for calculating amortizations and generating amortization schedules',
    python_requires='<4,>=3.6.2',
    project_urls={"repository": "https://github.com/roniemartinez/amortization"},
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    license='MIT',
    keywords='amortization',
    classifiers=['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: MIT License', 'Topic :: Office/Business :: Financial :: Accounting', 'Topic :: Scientific/Engineering :: Mathematics', 'Topic :: Software Development :: Libraries :: Python Modules', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: Implementation :: CPython'],
    entry_points={"console_scripts": ["amortize = amortization.amortize:main"]},
    packages=['amortization'],
    package_dir={"": "."},
    package_data={},
    install_requires=['tabulate==0.*,>=0.8.6'],
    extras_require={"dev": ["autoflake==1.*,>=1.3.1", "black==21.*,>=21.5.0.b1", "codecov==2.*,>=2.0.16", "dephell==0.*,>=0.8.3", "flake8==3.*,>=3.7.9", "isort==5.*,>=5.7.0", "mypy==0.*,>=0.812.0", "pytest==6.*,>=6.2.2", "pytest-cov==2.*,>=2.8.1", "tomlkit==0.7.0"]},
)