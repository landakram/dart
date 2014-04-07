import os
from setuptools import setup

def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(name='needle',
      version='1.0',
      author='Mark Hudnall',
      author_email='me@markhudnall.com',
      license='MIT',
      description='Turn URL variables into models.',
      long_description=read('README.rst'),
      py_modules=['needle'],
      install_requires=['flask-sqlalchemy'])
