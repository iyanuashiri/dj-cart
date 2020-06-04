import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name='dj-cart',
        version='1.0.0',
        description='A simple shopping cart for Django.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        maintainer='Iyanuoluwa Ajao',
        maintainer_email='ajaoiyanu@gmail.com',
        license="MIT",
        url='https://github.com/iyanuashiri/dj-cart',
        packages=['cart', 'cart.migrations'],
        install_requires=[
            'Django>=1.1',
        ],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Framework :: Django",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        test_suite="tests.run_tests.run_tests"
     )