from setuptools import setup, find_packages

name = '<%= project_name %>'
description = ('')
version = '0.1.0'

setup(
    name=name,
    version=version,
    description=description,
    packages=find_packages(),
    install_requires=[
        'morepath>=0.14',
    ],
    entry_points=dict(
        console_scripts=[
            'run-app = <%= project_name %>.__main__:run',
        ],
    )
)