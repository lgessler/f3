import setuptools
from f3.version import Version


setuptools.setup(name='f3',
                 version=Version('0.0.1').number,
                 description='Command line tool for extracting word Frequencies From Files',
                 long_description=open('README.md').read().strip(),
                 author='Luke Gessler',
                 author_email='lukegessler@gmail.com',
                 url='https://github.com/lgessler/f3',
                 py_modules=['f3'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='word frequency',
                 classifiers=[],
                 entry_points={
                     'console_scripts':{
                         'f3 = f3.__main__:main'
                     }
                 },
                 packages=setuptools.find_packages())
