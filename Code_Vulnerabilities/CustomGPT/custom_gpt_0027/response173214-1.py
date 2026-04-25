
from setuptools import setup, Extension

module1 = Extension('demo',
                    sources=['demo.c'])

setup(name='DemoPackage',
      version='1.0',
      description='A simple example package',
      ext_modules=[module1])
