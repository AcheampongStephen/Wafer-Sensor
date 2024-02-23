from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='The goal is to build a machine learning model which predicts whether a wafer needs to be replaced or not(i.e., whether it is working or not) based on the inputs from various sensors. There are two classes: +1 and -1.',
    author='Stephen Acheampong',
    license='MIT',
)
