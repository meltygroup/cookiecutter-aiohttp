#!/usr/bin/env python{{ cookiecutter.python_version }}

from setuptools import setup, find_packages

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
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    test_suite='tests',
    version='{{ cookiecutter.project_version }}',
    license='Proprietary',
    zip_safe=False,
    entry_points= {
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}:main'
        ]
    }
)