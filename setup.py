from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mindmelting.powerpal",
    version="0.2.1",
    author="Lawrence Hunt",
    author_email="lawrence.hunt@gmail.com",
    url="https://github.com/mindmelting/powerpal",
    description="Simple Python client for calling Powerpal Readings API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test"]),
    python_requires='>=3.6',
    install_requires=["aiohttp>=3.0.0"],
)
