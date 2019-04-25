import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datautil",
    version="0.0.1",
    author="City of Austin",
    author_email="transportation.data@austintexas.gov",
    description="Miscellaneous utilities for manipulating data types.",
    install_requires=[
      'requests',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cityofaustin/atd-utils-data",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", 
    ),
)

