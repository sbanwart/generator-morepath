"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html

This is an empty setup.py for this module. The project name will be
pre-populated by the generator.
"""

from setuptools import setup, find_packages

setup(
    name='<%= project_name %>',
    version='0.1.0',
    description='',
    long_description='',
    url='',
    author='',
    author_email='',
    license='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(),
    install_requires=[
        'morepath>=0.14',
    ],
    entry_points={
        'console_scripts': [
            'run-app=<%= project_name %>.__main__:run',
        ],
    },
)
