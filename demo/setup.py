#!/usr/bin/env python
import io

from setuptools import setup, find_packages


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='toga-demo',
    version='0.3.0.dev18',
    description='A demonstration of the capabilities of the Toga widget toolkit.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://beeware.org/toga-demo',
    include_package_data=True,
    packages=find_packages(),
    python_requires='>=3.5',
    package_data={
        'toga_demo': ['resources/*.icns', 'resources/*.png'],
    },
    install_requires=[
        'toga==0.3.0.dev18'
    ],
    entry_points={
        'console_scripts': [
            'toga-demo = toga_demo.__main__:run',
        ]
    },
    license='New BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    options={
        'app': {
            'formal_name': 'Toga Demo',
            'bundle': 'org.beeware',
        },
        'ios': {
            'app_requires': [
                'toga-ios==0.3.0.dev18',
            ]
        },
        'django': {
            'app_requires': [
                'toga-django==0.3.0.dev18',
            ]
        },
        'macos': {
            'app_requires': [
                'toga-cocoa==0.3.0.dev18',
            ]
        },
        'linux': {
            'app_requires': [
                'toga-gtk==0.3.0.dev18',
            ]
        },
        'windows': {
            'app_requires': [
                'toga-winform==0.3.0.dev18',
            ]
        },
        'android': {
            'app_requires': [
                'toga-android==0.3.0.dev18',
            ]
        }
    }
)
