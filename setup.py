import os
from setuptools import setup, find_packages

VERSION = '0.1.0'
PATH = os.path.dirname(os.path.abspath(__file__))

install_requires = [
    'robotframework',
    'jsonschema',
]


def read(fname):
    return open(os.path.join(PATH, fname)).read()


setup(
    name='robot-jsonschemalibrary',
    version=VERSION,
    description='A Robot Framework library for JSON Schema validation.',
    long_description=read('README.rst'),
    url='',
    author='hypc',
    author_email='h_yp00@163.com',
    license='MIT',
    keywords='robotframework json jsonschema',
    project_urls=[],
    packages=find_packages(exclude=['docs', 'tests*', 'example']),
    install_requires=install_requires,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Robot Framework',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
