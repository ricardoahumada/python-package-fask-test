
from setuptools import setup, find_packages

setup(
    name='python-package-flask-test',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python-package-flask-test',
    long_description='An example python-package-flask-test',
    install_requires=['numpy'],
    url='https://github.com/ricardoahumada/python-package-flask-test',
    author='Ricardo Ahumada',
    author_email='ricardo@enmotionvalue.com'
)
