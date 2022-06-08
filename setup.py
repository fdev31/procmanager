from setuptools import setup

setup(
   name='procmanager',
   version='1.0.1',
   description='Helps starting & stopping programs',
   author='Fabien Devaux',
   url='https://github.com/fdev31/procmanager',
   author_email='fdev31@gmail.com',
   packages=['procmanager'],  # would be the same as name
   scripts=['scripts/procmgr'],
   )
