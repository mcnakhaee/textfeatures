from setuptools import setup
import setuptools
setup(name='textfeatures',
      version='0.1.2',
      url="https://github.com/mcnakhaee/palmerpenguins",
      description="A python package to extract features from text data ",
      long_description=open('DESCRIPTION.rst').read(),
      author='Muhammad Chenariyan Nakhaee',
      author_emai='mcnakhaee@gmail.com',
      packages = ['textfeatures'],
      install_requires=['pandas', 'spacy','pyenchant','textblob','nltk'],
      include_package_data=True,
      package_data={'': ['data/*.csv']},
      )
