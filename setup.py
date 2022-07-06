import setuptools

setuptools.setup(
   name='space remover',
   version='0.1',
   description='A simple tool that automatize removing any unwanted leading or lagging space from a column of a excel file',
   author='Khandoker Tanjim Ahammad',
   author_email='alttanjim@gmail.com',
   packages=setuptools.find_packages(),  #same as name
   classifiers=[ "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License", 
    "Operating System :: OS Independent", ],
)