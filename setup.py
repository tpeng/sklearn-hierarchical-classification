#!/usr/bin/env python
from setuptools import find_packages, setup


project = "sklearn-hierarchical-classification"
version = "1.3.2"


setup(
    name=project,
    version=version,
    description="Hierarchical classification interface extensions for scikit-learn",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Globality Engineering",
    author_email="engineering@globality.com",
    url="https://github.com/globality-corp/sklearn-hierarchical-classification",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "networkx==2.2",
        "numpy==1.16.6",
        "scikit-learn==0.19.1",
        "scipy==0.19.1",
    ],
    setup_requires=[
        "nose>=1.3.7",
    ],
    extras_require={
        "test": [
            "PyHamcrest>=1.9.0",
            "coverage>=3.7.1",
            "inflect>=4.0.0",
            "parameterized>=0.7.1",
        ],
    },
)
