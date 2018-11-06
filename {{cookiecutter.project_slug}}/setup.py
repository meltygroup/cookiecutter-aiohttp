#!/usr/bin/env python{{ cookiecutter.python_version }}

from setuptools import setup

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: {{ cookiecutter.python_version }}',
    ],
    description='{{ cookiecutter.project_short_description }}',
    long_description=long_description,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=['{{ cookiecutter.project_slug }}'],
    test_suite='tests',
    version='{{ cookiecutter.project_version }}',
    license='Proprietary',
    zip_safe=False,
    install_requires=[
        'aiohttp==3.3.2',
        'toml==0.9.4'
    ],
    extras_require={
        'dev': [
            'pytest==3.6.3',
            'pytest-cov==2.5.1',
            'pytest-aiohttp==0.3.0',
            'flake8==3.5.0',
            'pylint==1.8.2',
            'black==18.6b4',
            'bandit==1.4.0',
            'mypy==0.610',
            'detox==0.12'
        ]
    },
    entry_points= {
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}:main'
        ]
    },
)
