from setuptools import setup

setup(
   name='boolog',
   version='1.0',
   description='A log of a blog by boo',
   author='Randy Boo',
   author_email='boo13bot@gmail.com',
   packages=['boolog'],  #same as name
   install_requires=['flask', 'streamlink'], #external packages as dependencies
)