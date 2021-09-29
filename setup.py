from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="powerpal",
    version="0.1.0",
    author="Lawrence Hunt",
    url="https://github.com/mindmelting/powerpal",
    description="Python client for calling Powerpal API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test"]),
    python_requires='>=3.6',
    install_requires=["aiohttp>=3.0.0"],
)
