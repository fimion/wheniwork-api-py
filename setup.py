from distutils.core import setup


with open('./requirements.txt') as f:
    requirements = f.read().splitlines()


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name='wheniwork',
    packages=['wheniwork'],  # this must be the same as the name above
    version='0.1',
    description='A library for interfacing with the WhenIWork.com API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alex Riviere',
    author_email='fimion@gmail.com',
    url='https://github.com/fimion/wheniwork-api-py',
    download_url='https://github.com/fimion/wheniwork-api-py/tarball/0.1',
    keywords=['wheniwork', 'api'],
    classifiers=[],
    install_requires=requirements,
)
