from setuptools import setup, find_packages
from setuptools.command.install import install
from codecs import open
from os import path
from unittest import TestLoader

class PostInstallMessage(install):
    def run(self):
        print("DEPRECATION WARNING: The swiftype_app_search package has been deprecated and replaced by elastic-app-search")
        install.run(self)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

here = path.abspath(path.dirname(__file__))
about = {}
with open(path.join(here, 'swiftype_app_search', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='swiftype elastic app search api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'requests',
        'PyJWT'
    ],
    tests_require=[
        'requests_mock',
        'future'
    ],
    test_suite='tests',
    cmdclass={
        'install': PostInstallMessage,
    }
)
