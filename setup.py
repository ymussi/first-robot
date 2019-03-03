#coding: utf-8

from setuptools import setup, find_packages


# install requirements of the project
with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='ROBOT',
      version="0.0.1",
      description="",
      url="",
      author="Yuri Mussi",
      author_email="ymussi@gmail.com",
      license="BSD",
      keywords="robot mail",
      packages=find_packages(),
      package_data={'robot.parsers': ['*/*.json', '*/*xml']},
      zip_safe=False
      ),
