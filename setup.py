from setuptools import setup, find_packages

setup(
    name='predictpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    description='Package for predict',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas>=0.20.0'],
    url='https://github.com/CallinR/analyse_predict.git',
    author='<Jay Ramesh>',
    author_email='<jayramesh01@gmail.com>' 
)