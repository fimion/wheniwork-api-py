from setuptools import find_packages, setup
from wheniwork.version import VERSION_NUMBER

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name='wheniwork',
    packages=find_packages(exclude=("tests", "docs",)),
    version=VERSION_NUMBER,
    description='A library for interfacing with the WhenIWork.com API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author='Alex Riviere',
    author_email='fimion@gmail.com',
    url='https://github.com/fimion/wheniwork-api-py',
    download_url='https://github.com/fimion/wheniwork-api-py/tarball/{version}'
                .format(version=VERSION_NUMBER),
    keywords=['wheniwork', 'api'],
    classifiers=[],
    install_requires=requirements,
)
